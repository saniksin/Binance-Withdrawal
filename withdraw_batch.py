from settings import set_coin, set_network, set_address_withdraw_value, print_info, accept_withdraw


def withdraw_func(client, address_list):
    try:
        # Получаем тикер, баланс и сеть для вывода
        asset, balance = set_coin(client)
        network = set_network()
    
        # Пользователь вводит сумму для вывода на каждый кошелек
        amount, withdraw_value = set_address_withdraw_value(balance, address_list)

        # Выводим окончательную информацию для проверки и ожидаем подтверждения пользователя
        answer = print_info(asset, network, withdraw_value, address_list)

        # Зависимо от резутата ввода пользователя осуществляем вывод
        if answer.lower() == 'да':
            accept_withdraw(amount=amount, address_list=address_list, \
                            client=client, asset=asset, network=network)
        else:
            print('Вы не подтвердили вывод.')
            print('Программа завершена.')
    except KeyboardInterrupt:
        print('\nВы успешно вышли из программы')
