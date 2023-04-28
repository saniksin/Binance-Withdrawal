from settings import set_coin, set_network, set_address_withdraw_value, print_info, accept_withdraw


def withdraw_random_func(client, address_list):
    try:
        print("ВНИМАНИЕ! ПРИ ВЫВОДЕ РАНДОМОМ ОСТАВЛЯЙТЕ НА 1.5% БОЛЬШЕ ДЕНЕГ ЧЕМ ПЛАНИРОВАЛИ ВЫВОДИТЬ!")

        # Получаем тикер, баланс и сеть для вывода
        asset, balance = set_coin(client)
        network = set_network()

        # Пользователь вводит сумму для вывода на каждый кошелек
        amount, withdraw_value = set_address_withdraw_value(balance, address_list)

        # Выводим окончательную информацию для проверки и ожидаем подтверждения пользователя
        answer = print_info(asset, network, withdraw_value, address_list, random=True)

        # Зависимо от резутата ввода пользователя осуществляем вывод
        if answer.lower() == 'да':
            accept_withdraw(amount=amount, address_list=address_list, \
                client=client, asset=asset, network=network, random=True)
        else:
            print('Вы не подтвердили вывод.')
            print('Программа завершена.')
    except KeyboardInterrupt:
        print('\nВы успешно вышли из программы')
