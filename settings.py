# Список всех функций и проверок для вывода
from binance.enums import *
from binance.exceptions import BinanceAPIException
import secrets


# Функция для проверки статуса 
def check_coin(all_coins_info, coin, network):
    # Проверяем статус монеты и возращаем словарь значений
    for coin_info in all_coins_info:
        if coin_info['coin'] == coin:
            for network_data in coin_info['networkList']:
                if network_data['network'] == network:
                    info = {
                        'withdraw_info': network_data['withdrawEnable'],
                        'deposit_info': network_data['depositEnable'],
                        'withdrawMin': str(network_data['withdrawMin']),
                        'withdrawFee': str(network_data['withdrawFee']),
                    }
                    return info
                
    # Выводим сообщение, если информация о монете и сети не найдена
    print(f"Информация о монете {coin} в сети {network} не найдена.")

# Функция для вывода информации о статусе криптовалюты
def print_coin_info(coin, network, info):
    print('-'*70)
    all_info = f"""\nТекущий статус {coin} в сети {network}:
        Комиссия за вывод: {info['withdrawFee']} {coin}
        Минимальная сумма вывода: {info['withdrawMin']} {coin}
        Статус вывода: {info['withdraw_info']}
        Статус депозита: {info['deposit_info']}
            """
    print(all_info)
    print('-'*70)

# Пользователь вводит тикер криптовалюты
def set_coin(client, withdraw_status=True):
    try:
        asset=str(input("""Введите тикер криптовалюты которую хотите вывести. (ETH/USDT/USDC/BNB/MATIC)
    [+] Ваш ввод: """))
        if withdraw_status:
            balance = client.get_asset_balance(asset=f'{asset}')
            print(f"""Ваш текущий баланс {balance['asset']}:
    Доступный: {balance['free']}
    Залоченый: {balance['locked']}""")
            return asset.strip().upper(), balance
        else:
            return asset.strip().upper()
    except TypeError:
        print('Ошибка: неверный тикер криптовалюты или проблемы с подключением к серверу Binance')
        raise SystemExit(1)

# Пользователь выбирает сеть
def set_network():
    # Выбираем сеть для вывода
    network_list = ['ETH', 'BSC', 'OPTIMISM', 'ARBITRUM', 'MATIC']
    network = input('''Введите название сети криптовалюты для вывода.
Доступные сети: ETH, BSC, OPTIMISM, ARBITRUM, MATIC.
    [+] Ваш ввод: ''')
    network = network.strip().upper()
    if network not in network_list:
        print('Неверно введена сеть криптовалюты')
        raise SystemExit(1)
    return network

# Проверка на тип данных
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Информация для вывода
def withdraw_status_info(asset, withdraw_fee, withdraw_min, withdraw_status):
    print('-'*70)
    print (f"""
    Комиссия за каждый вывод: {withdraw_fee} {asset}.
    Минимальное кол-во для вывода: {withdraw_min} {asset}.
    Доступность вывода: {withdraw_status}.
    """)
    print('-'*70)

# Проверяем статус криптовалюты
def check_coin_status(client, asset, network):
    asset_details = client.get_all_coins_info()
    info = check_coin(asset_details, coin=asset, network=network)
    if info:
        withdraw_fee, withdraw_min, withdraw_status = info['withdrawFee'], info['withdrawMin'], info['withdraw_info']
        withdraw_status_info(asset, withdraw_fee, withdraw_min, withdraw_status)
        if not withdraw_status: 
            print(f"Сейчас на бирже временно не доступен вывод {asset} в сети {network}")
            raise SystemExit(1)
        return float(withdraw_fee), float(withdraw_min)
    else:
        print(f'{asset} недоступен для вывода в сети {network}!')
        raise SystemExit(1)

# Проверяем корректным ли является вывод
def check_amount_value(withdraw_fee, withdraw_min, amount, withdraw_fee_value,
                       withdraw_value, balance_now=None, multi=False, 
                       address_list=None, random=False, withdraw_amount=None):
    if (amount + withdraw_fee) < withdraw_min:
        formatted_ammount = '{:.8f}'.format(amount)
        print(f'Ошибка: указанное количество криптовалюты {formatted_ammount} + {withdraw_fee} должно быть больше минимально \
допустимого значения на вывод {withdraw_min}.')
        raise SystemExit(1)
    if (amount + withdraw_fee) > balance_now:
        print(f"Ошибка: указанное количество криптовалюты для вывода {amount} \
+ комиссия {withdraw_fee} превышает доступный баланс {balance_now} .")
        raise SystemExit(1)
    if multi is not None and multi:
        if balance_now < (withdraw_value + withdraw_fee_value):
            print("Ошибка: вам не хватит денег для вывода на все кошельки")
            raise SystemExit(1)
    elif random is not None and random:
        if sum(withdraw_amount) + (len(address_list) * withdraw_fee) > balance_now:
            print("Ошибка: вам не хватит денег для вывода на все кошельки")
            raise SystemExit(1)
    else:
        if (withdraw_value * len(address_list)) + (len(address_list) * withdraw_fee) > balance_now:
            print("Ошибка: вам не хватит денег для вывода на все кошельки")
            raise SystemExit(1)
        


# Пользователь задает сумму на вывод
def set_address_withdraw_value(withdraw_fee, withdraw_min, balance, address_list, 
                               multi=False, random=False):
    print('Введите кол-во криптовалюты для вывода. Это может быть как целое число так и дробное число.')
    # Пользователь задает значение для всех кошельков вручную
    withdraw_value = 0
    withdraw_fee_value = withdraw_fee * len(address_list)
    if multi:
        withdraw_amount = []
        for address in address_list:
            amount = input(f'Введите сумму вывода для адреса {address}\n    [+] Ваш ввод: ')
            while not is_float(amount):
                print('Введенное значение должно быть числом! Попробуйте еще раз')
                amount = input(f'Введите сумму вывода для адреса {address}\n    [+] Ваш ввод: ')
            amount = float(amount)
            withdraw_amount.append(amount)
            withdraw_value += amount
            check_amount_value(withdraw_fee, withdraw_min, amount, withdraw_fee_value,
                               multi=True, balance_now=float(balance['free']), 
                               withdraw_value=withdraw_value)

        return withdraw_amount, withdraw_value
    else:
        amount = input('    [+] Ваш ввод: ')
        while not is_float(amount):
            print('Введенное значение должно быть числом! Попробуйте еще раз')
            amount = input('    [+] Ваш ввод: ')
        amount = float(amount)
        withdraw_value += amount

        if random:
            clone_amount = amount
            i = 0
            withdraw_amount = []
            while i < len(address_list):
                amount = clone_amount
                random_value = secrets.randbelow(151) + 10000
                amount = round(amount/100 * random_value/100, 8)
                withdraw_amount.append(float(amount))
                i += 1
            withdraw_value = (sum(withdraw_amount))
            check_amount_value(withdraw_fee, withdraw_min, amount, withdraw_fee_value, balance_now=float(balance['free']), 
                           withdraw_value=withdraw_value, address_list=address_list, random=True, withdraw_amount=withdraw_amount)
            return amount, withdraw_value, withdraw_amount
    
        check_amount_value(withdraw_fee, withdraw_min, amount, withdraw_fee_value, balance_now=float(balance['free']), 
                           withdraw_value=withdraw_value, address_list=address_list)
        return amount, withdraw_value


# Обрабатываем ответ пользователя
def get_answer():
    print('Все верно? Введите "да" чтобы продолжить')
    answer = input('    [+] Ваш ввод: ')
    return answer

# Выводим информацию чтобы пользователь ее проверил:
def print_withdraw_info(asset, network, withdraw_fee, withdraw_value, address_list, withdraw_amount=None, multi=False, random=False):

    print('-'*70)
    print(f'''Проверяем информацию: 
    
    Выводим: {asset}.
    Сеть: {network}.
    Количество адресов: {len(address_list)}
    Комиссия за вывод: {round(len(address_list) * withdraw_fee, 10)} {asset}''')

    if multi is not None and multi:
        print(f'''    Общая сумма вывода: {round(sum(withdraw_amount), 10)} {asset}.\n{'-'*70}
    Информация по кошелькам: ''')
        i = 0
        while i < len(address_list):
            print(f"{' '*8}{address_list[i]} - {withdraw_amount[i]} + {withdraw_fee} {asset}.")
            i += 1
        print(f'\n    Общая сумма вывода+комса: {round(withdraw_value, 10) + (round(len(address_list) * withdraw_fee, 10))}')
        print('-'*70)
        answer = get_answer()
        return answer
    else:
        if random is not None and random:
            print(f'''    Общая сумма вывода: {round(withdraw_value, 10)} {asset} + рандомное значение для каждого вывода до 1.5%.
    Общая сумма вывода+комса: {round(withdraw_value, 10) + (round(len(address_list) * withdraw_fee, 10))}''')
        else:
            print(f'''    Общая сумма вывода: {round(withdraw_value, 10)} {asset}.
    Общая сумма вывода+комса: {round((withdraw_value * len(address_list)), 10) + (round(len(address_list) * withdraw_fee, 10))}''')
        print('-'*70)
        answer = get_answer()
        return answer
    
# Функция вывода криптовалюты
def accept_withdraw(address_list, client, asset, network, withdraw_fee, amount=None,
                    withdraw_amount=None, multi=False, random=False):
    # Вывод криптовалюты
    try:
        print('Начинаем вывод криптовалюты...')
        # Если пользователь устанавливает вывод для каждого кошелька вручную
        if multi:
            i = 0
            while i < len(address_list):
                full_amount = round(withdraw_amount[i] + withdraw_fee, 6)
                tx_id = client.withdraw(coin=asset, address=address_list[i], amount=full_amount, network=network, timestamp=60000)
                print(f"[+] Транзакция #{i+1} успешно отправлена на адрес {address_list[i]} в сети {network}.\n"
                      f"Сумма вывода {withdraw_amount[i]} {asset} + комиссия за вывод {withdraw_fee} = {full_amount} {asset}")
                i += 1
        # Если пользователь выбрал вывод рандомом
        elif random:
            for i, address in enumerate(address_list):
                full_amount = round(withdraw_amount[i] + withdraw_fee, 6)
                print(full_amount)
                tx_id = client.withdraw(coin=asset, address=address_list[i], amount=full_amount, network=network, timestamp=60000)
                print(f"[+] Транзакция #{i+1} успешно отправлена на адрес {address_list[i]} в сети {network}.\n"
                      f"Сумма вывода {withdraw_amount[i]} {asset} + комиссия за вывод {withdraw_fee} = {full_amount} {asset}")
                i += 1
        else:
            for i, address in enumerate(address_list):
                full_amount = round(amount + withdraw_fee, 6)
                print(full_amount)
                tx_id = client.withdraw(coin=asset, address=address, amount=full_amount, network=network, timestamp=60000)
                print(f"[+] Транзакция #{i+1} успешно отправлена на адрес {address} в сети {network}. Сумма вывода {amount} + {withdraw_fee} = {full_amount} {asset}")

        print('-'*70)
        print('\nПрограмма успешно завершила вывод криптовалюты.')

    except BinanceAPIException as e:
        print(f"Ошибка при выводе криптовалюты: {e}")
        print(f"Возникла ошибка при выводе на адрес {address_list[i]}")
        print('Программа завершена')

   
