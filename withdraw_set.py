from settings import *


def withdraw_set_func(client, address_list):
    try:
        # Получаем тикер, баланс и сеть для вывода
        asset, balance = set_coin(client)
        network = set_network()

        # Получаем cтатус вывода
        withdraw_fee, withdraw_min = check_coin_status(client, asset, network)

        # Пользователь вводит сумму для вывода на каждый кошелек
        withdraw_amount, withdraw_value = set_address_withdraw_value(withdraw_fee, withdraw_min, balance, address_list, multi=True)

        # Выводим окончательную информацию для проверки и ожидаем подтверждения пользователя
        answer = print_withdraw_info(asset, network, withdraw_fee, withdraw_value, address_list, withdraw_amount, multi=True)

        # Зависимо от резутата ввода пользователя осуществляем вывод
        if answer.lower() == 'да':
            accept_withdraw(address_list=address_list, client=client, \
                            asset=asset, withdraw_amount=withdraw_amount, \
                            network=network, withdraw_fee=withdraw_fee, multi=True)
        else:
            print('Вы не подтвердили вывод.')
            print('Программа завершена.')
    except KeyboardInterrupt:
        print('\nВы успешно вышли из программы')

