# Список всех функций и проверок для вывода
from binance.enums import *
from binance.exceptions import BinanceAPIException
import secrets

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

# Делаем проверки
def check_amount_value(amount, balance, multi=False, balance_now=None, \
                                    withdraw_value=None, address_list=None):
    if amount <= 0:
        print('Ошибка: количество криптовалюты для вывода должно быть положительным числом.')
        raise SystemExit(1)
    if amount > float(balance['free']):
        print('Ошибка: количество криптовалюты для вывода превышает доступный баланс.')
        raise SystemExit(1)
    if multi is not None and multi:
        if balance_now < withdraw_value:
            print("Ошибка: вам не хватит денег для вывода на все кошельки")
            raise SystemExit(1)
    else:
        if amount * len(address_list) > float(balance['free']):
            print("Ошибка: вам не хватит денег для вывода на все кошельки")
            raise SystemExit(1)

# Пользователь вводит значение для каждого кошелька:
def set_address_withdraw_value(balance, address_list, multi=False):
    print('Введите кол-во криптовалюты для вывода. Это может быть как целое число так и дробное число.')
    # Пользователь задает значение для всех кошельков вручную
    if multi is not None and multi:
        withdraw_amount = []
        balance_now = float(balance['free'])
        withdraw_value = 0
        for adress in address_list:
            amount = input(f'Сумма вывода для адреса {adress}\n    [+] Ваш ввод: ')
            # Обрабатываем если пользователь ввел не числовое значение для вывода
            while not is_float(amount):
                print('Введенное значение должно быть числом! Попробуйте еще раз')
                amount = input(f'Сумма вывода для адреса {adress}\n    [+] Ваш ввод: ')
            amount = float(amount)

            # Делаем проверку
            check_amount_value(amount, balance, multi=True, balance_now=balance_now, withdraw_value=withdraw_value)

            # Добавляем введенное значение в список
            withdraw_amount.append(amount)
            withdraw_value += amount

        return withdraw_amount, withdraw_value
    
    # В остальных случаях
    else:
        amount = input('    [+] Ваш ввод: ')
        # Обрабатываем если пользователь ввел не числовое значение для вывода
        while not is_float(amount):
            print('Введенное значение должно быть числом! Попробуйте еще раз')
            amount = input('    [+] Ваш ввод: ')
        amount = float(amount)

        withdraw_value = amount * len(address_list)

        check_amount_value(amount, balance, address_list=address_list)

        return amount, withdraw_value

# Обрабатываем ответ пользователя
def get_answer():
    print('Все верно? Введите "да" чтобы продолжить')
    answer = input('    [+] Ваш ввод: ')
    return answer

# Выводим информацию чтобы пользователь ее проверил:
def print_info(asset, network, withdraw_value, address_list=None, withdraw_amount=None, multi=False, random=False):

    print('-'*70)
    print(f'''Проверяем информацию: 
    
    Выводим: {asset.upper()}.
    Сеть: {network}.''')
    if multi is not None and multi:
        print(f'''    Общая сумма вывода: {round(withdraw_value, 10)} {asset}.\n{'-'*70}
    Информация по кошелькам: ''')
        i = 0
        while i < len(address_list):
            print(f"{' '*8}{address_list[i]} - {withdraw_amount[i]} {asset}.")
            i += 1
        print('-'*70)
        answer = get_answer()
        return answer
    else:
        if random is not None and random:
            print(f'    Общая сумма вывода: {round(withdraw_value, 10)} {asset} + рандомное значение для каждого вывода до 1.5%.')
        else:
            print(f'    Общая сумма вывода: {round(withdraw_value, 10)} {asset}.')
        print('-'*70)
        answer = get_answer()
        return answer
    
# Функция вывода криптовалюты
# accept_withdraw(, , , , , =)
def accept_withdraw(address_list, client, asset, network, amount=None, withdraw_amount=None, multi=False, random=False):
    # Вывод криптовалюты
    try:
        print('Начинаем вывод криптовалюты...')
        # Если пользователь устанавливает вывод для каждого кошелька вручную
        if multi:
            i = 0
            while i < len(address_list):
                tx_id = client.withdraw(coin=asset, address=address_list[i], amount=withdraw_amount[i], network=network, transactionFeeFlag=False, timestamp=60000)
                print(f"[+] Транзакция #{i+1} успешно отправлена на адрес {address_list[i]} в сети {network}. Сумма вывода: {withdraw_amount[i]} {asset}")
                i += 1
        # Если пользователь выбрал вывод рандомом
        elif random:
            clone_amount = amount
            i = 0
            while i < len(address_list):
                amount = clone_amount
                random_value = secrets.randbelow(151) + 10000
                amount = round(amount/100 * random_value/100, 8)
                tx_id = client.withdraw(coin=asset, address=address_list[i], amount=amount, network=network, transactionFeeFlag=False, timestamp=60000)
                print(f"[+] Транзакция #{i+1} успешно отправлена на адрес {address_list[i]} в сети {network}. Cумма вывода: {amount} {asset}")
                i += 1
        else:
            for i, address in enumerate(address_list):
                tx_id = client.withdraw(coin=asset, address=address, amount=amount, network=network, transactionFeeFlag=False, timestamp=60000)
                print(f"[+] Транзакция #{i+1} успешно отправлена на адрес {address} в сети {network}")

        print('Программа успешно завершила вывод криптовалюты.')

    except BinanceAPIException as e:
        print(f"Ошибка при выводе криптовалюты: {e}")
        print(f"Возникла ошибка при выводе на адрес {address_list[i]}")
        print('Программа завершена')

   
