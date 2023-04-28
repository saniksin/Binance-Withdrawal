import dotenv
import os
dotenv.load_dotenv()

# API ключи
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

# Считываем список адресов
address_list = []
with open('address.txt') as address:
    address_list = [line.strip() for line in address.readlines()]

# Меню выбора пользователя
options = {
    1: 'Проверить cписок кошельков для вывода.',
    2: 'Проверить статус ввода/вывода для токена в сети.',
    3: 'Вручную указать сумму для каждого вывода на кошелек.',
    4: 'Вывести рандомную сумму (до +1.5% к тому что вы укажите) на все кошельки. (Рекомендуемый способ вывода)',
    5: 'Вывести одинаковую сумму на все кошельки. (Не рекомендуемый способ вывода)'
}
