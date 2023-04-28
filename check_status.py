from binance.exceptions import BinanceAPIException
import sys
from settings import set_coin, set_network, check_coin, print_coin_info

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
        print_coin_info(coin, network, info)

    except KeyboardInterrupt:
        print('\nВы успешно вышли из программы')    
    except:
        print('\nПрограмма завершена')
        sys.exit()