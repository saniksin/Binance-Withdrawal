from settings import *


def withdraw_random_func(client, address_list):
    try:
        print("ВНИМАНИЕ! ПРИ ВЫВОДЕ РАНДОМОМ ОСТАВЛЯЙТЕ НА 1.5% БОЛЬШЕ ДЕНЕГ ЧЕМ ПЛАНИРОВАЛИ ВЫВОДИТЬ!")

        # Получаем тикер, баланс и сеть для вывода
        asset, balance = set_coin(client)
        network = set_network()

        # Получаем cтатус вывода
        withdraw_fee, withdraw_min = check_coin_status(client, asset, network)

        # Пользователь вводит сумму для вывода на каждый кошелек
        amount, withdraw_value, withdraw_amount = set_address_withdraw_value(withdraw_fee, withdraw_min, balance, address_list, random=True)

        # Выводим окончательную информацию для проверки и ожидаем подтверждения пользователя
        answer = print_withdraw_info(asset, network, withdraw_fee, withdraw_value, address_list, random=True)

        # Зависимо от резутата ввода пользователя осуществляем вывод
        if answer.lower() == 'да':
            accept_withdraw(withdraw_amount=withdraw_amount, withdraw_fee=withdraw_fee, amount=amount, address_list=address_list, \
                client=client, asset=asset, network=network, random=True)
        else:
            print('Вы не подтвердили вывод.')
            print('Программа завершена.')
    except KeyboardInterrupt:
        print('\nВы успешно вышли из программы')
