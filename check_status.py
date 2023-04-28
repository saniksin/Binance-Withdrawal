from binance.exceptions import BinanceAPIException
import sys
from settings import set_coin, set_network

# Функция для вывода информации
def print_info(coin, network, info):
    print('-'*70)
    all_info = f"""\nТекущий статус {coin} в сети {network}:
        Комиссия за вывод: {info['withdrawFee']} {coin}
        Минимальная сумма вывода: {info['withdrawMin']} {coin}
        Статус вывода: {info['withdraw_info']}
        Статус депозита: {info['deposit_info']}
            """
    print(all_info)
    print('-'*70)
    

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


# Функция для сбора данных
def input_info(client):
    try:
        # Получаем тикер и сеть для проверки
        coin = set_coin(client, withdraw_status=False)
        network = set_network()

        # Пытаемся получить список всех монет и обрабатываем данные которые ввел пользователь.
        try:
            all_coins_info = client.get_all_coins_info()
            info = check_coin(all_coins_info, coin, network)
        except BinanceAPIException as e:
            print(f"Ошибка при получении информации о {network} сети для {coin}: {e}")
            sys.exit()

        # Вывод сообщения на экран пользователю.
        print_info(coin, network, info)

    except KeyboardInterrupt:
        print('\nВы успешно вышли из программы')    
    except:
        print('\nПрограмма завершена')
        sys.exit()