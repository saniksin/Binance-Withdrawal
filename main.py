from binance.client import Client
from config import API_KEY, API_SECRET, address_list, options
from check_status import input_info
from withdraw_batch import withdraw_func
from withdraw_set import withdraw_set_func
from withdraw_random import withdraw_random_func


def main():
    try:
        print('-'*70)
        print("Добро пожаловать! В любой момент нажмите СTRL+C для выхода из программы.")
        print('-'*70)
        # Инициализация клиента Binance
        client = Client(API_KEY, API_SECRET, requests_params={'timeout': 5})
        
        # Выбираем действие
        print('Что вы хотите сделать? Доступные опции:')
        for key, value in options.items():
            print(f'  > {key}. {value}')
        print('-'*70)
        print('Введите число.')
        print('-'*70)

        # Проверяем тип данных который ввел пользователь
        answer = input('[+] Ваш ввод: ')
        while not answer.isdigit():
            print('Введенное значение должно быть числом! Попробуйте еще раз')
        answer = int(answer)

        # Проверяем кошельки которые ввел пользователь
        if answer == 1:
            print('-'*50)
            print('Список ваших кошельков:')
            print('-'*50)
            for address in address_list:
                print(f'{address}')
            print('-'*50)
        
        # Проверяем статус монет на ввод/вывод
        elif answer == 2:
            input_info(client)

        # Выводим указанную пользователем сумму 
        elif answer == 3:
            withdraw_set_func(client, address_list)
        
        # Выводим указанную пользователем сумму + рандом (до 1.5%)
        elif answer == 4:
            withdraw_random_func(client, address_list)

        # Выводим на все кошельки указанную пользователем сумму
        elif answer == 5:
            withdraw_func(client, address_list)
        
    # Обработка при некорректном выборе/завершение программы
        else:
            print('Некорректный выбор. Програма завершена.')
    except KeyboardInterrupt:
        print('\nВы успешно вышли из программы')

if __name__ == "__main__":
    main()
    





