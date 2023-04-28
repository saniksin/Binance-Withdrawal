# Binance-Withdrawal ENG/RU

Binance-Withdrawal: An easy-to-use tool for automating cryptocurrency withdrawals to multiple wallets on the Binance platform.

Binance-Withdrawal: Простой в использовании инструмент для автоматизации вывода криптовалюты на несколько кошельков на платформе Binance.

# STEP 1
## Documentation for installing libraries and dependencies:

## Creating a virtual environment:

Windows:

   - Open PowerShell as an administrator.
   - Navigate to the project directory.
   - Install the virtual environment using the command "pip install virtualenv" (if asked to update the package manager, update it and install the virtual environment again).
   - In the project directory, create a virtual environment with the command "virtualenv venv".
   - Grant permission to run scripts with the command "Set-ExecutionPolicy RemoteSigned".
   - Activate the virtual environment with the command ".\venv\Scripts\activate".
   - If successful, the command line will display (venv) at the beginning.

Linux/MacOS:

   - Open the terminal.
   - Navigate to the project directory.
   - Install the virtual environment with the command "pip3 install virtualenv".
   - In the project directory, create a virtual environment with the command "python3 -m venv venv".
   - Activate the virtual environment with the command "source venv/bin/activate".
   - If successful, the terminal will display (venv) at the beginning.
   The command "chmod +x /path/to/directory/*" sets the execution rights (+x) for all files (*) in the specified directory (/path/to/directory). This allows you to run scripts and executables in this directory.
   - sudo chmod +x /path/to/directory/*

# ШАГ 1

## Документация по установке библиотек и зависимостей:

## Создание виртуального окружения:

Windows:

- Откройте PowerShell в имени администратора.
- Перейдите в директорию проекта.
- Установите виртуальное окружение командой "pip install virtualenv" (если просит обновить пакетный менеджер обновляем и еще раз устанавливаем виртуальное окружение).
- В директории проекта создайте виртуальное окружение командой "virtualenv venv".
- Дайте разрешение на выполнение скриптов "Set-ExecutionPolicy RemoteSigned"
- Активируйте виртуальное окружение командой ".\venv\Scripts\activate".
- Если все успешно, то в командной строке появится (venv) в начале.

Linux/MacOS:

- Откройте терминал.
- Перейдите в директорию проекта.
- Установите виртуальное окружение командой "pip3 install virtualenv".
- В директории проекта создайте виртуальное окружение командой "python3 -m venv venv".
- Активируйте виртуальное окружение командой "source venv/bin/activate".
- Если все успешно, то в терминале появится (venv) в начале.
Команда "chmod +x /path/to/directory/*" устанавливает права на исполнение (+x) для всех файлов (*) в указанной директории (/path/to/directory). Это позволяет запускать скрипты и исполняемые файлы в этой директории.
- sudo chmod +x /path/to/directory/*

# STEP 2

## Installing necessary dependencies in the virtual environment:

Windows:
  - Run the command "pip install -r requirements.txt".

Linux/MacOS:
 - Run the command "pip3 install -r requirements.txt".

# ШАГ 2

## Установка необходимых зависимостей в виртуальное окружение:

Windows:
- Выполните команду "pip install -r requirements.txt".

Linux/MacOS:
- Выполните команду "pip3 install -r requirements.txt".

# STEP 3

## Creating API keys on Binance:

!!! IMPORTANT !!! FOR SECURITY PURPOSES, CREATE A SEPARATE ACCOUNT FOR WITHDRAWALS TO WHICH YOU WILL ONLY TRANSFER THE AMOUNT YOU NEED FOR WITHDRAWAL !!!
!!! DO NOT KEEP PERSONAL FUNDS ON THE ACCOUNT YOU USE FOR WITHDRAWALS !!!

- Go to the Binance website and log in to your account.
- Go to the profile settings and select the "API Management" section.
- Click the "Create API" button, enter the confirmation code, and confirm the creation of a new key.
- After creating the key, you will receive an API key and a secret key. Save these keys in the .env file, as they will not be displayed in the future.
- Go to the API key restriction settings, add a trusted IP address. To check the IP address, you can use the website https://2ip.ru/.
- Then grant the API key permission to withdraw funds. Be sure to save these settings before completing!

# ШАГ 3

## Создание API-ключей на Binance:

!!! ВАЖНО !!! В ЦЕЛЯХ БЕЗОПАСТНОСТИ ЗАВЕДИТЕ ДЛЯ ВЫВОДА ОТДЕЛЬНЫЙ АККАУНТ НА КОТОРЫЙ БУДЕТЕ ПЕРЕВОДИТЬ ТОЛЬКО СУММУ НУЖНУЮ ВАМ ДЛЯ ВЫВОДА !!!
!!! НЕ ДЕРЖИТЕ ЛИЧНЫХ СРЕДСТВ НА АККАУНТЕ КОТОРЫЙ ВЫ ИСПОЛЬЗУЕТЕ ДЛЯ ВЫВОДА !!!

- Зайдите на сайт Binance и авторизуйтесь в своем аккаунте.
- Перейдите в настройки профиля и выберите раздел "Управление API".
- Нажмите на кнопку "Создать API", введите код подтверждения и подтвердите создание нового ключа.
- После создания ключа вы получите API-ключ и секретный ключ. Сохраните эти ключи в файл .env, так как они не будут отображаться в дальнейшем.
- Перейдите к настройкам ограничения API-ключа, добавьте доверенный IP-адрес. Для проверки IP-адреса можно использовать сайт https://2ip.ru/.
- Затем выдайте разрешение API ключу на вывод средств. Обязательно сохраните эти настройки перед завершением!

# STEP 4

## SETTING UP THE PROGRAM FOR OPERATION

Configure API_KEY/API_SECRET in config.py or .env. CHOOSE SOMETHING ONE!

- Write the API key in API_KEY.
- Write the secret API key in API_SECRET.

You should get something like this:

In config.py:

            API_KEY = 'jsdfhsa32-95872sdajfdsakfvh023945try72qtgsdajgvhasdsdfgjk325'
            API_SECRET = '834rdjsnfkna938457213985qdfjaskjdhfnd1208954r715r7fesdkjfnjs'

In .env:

            API_KEY=jsdfhsa32-95872sdajfdsakfvh023945try72qtgsdajgvhasdsdfgjk325
            API_SECRET=834rdjsnfkna938457213985qdfjaskjdhfnd1208954r715r7fesdkjfnjs


## Add your addresses to address.txt.

Add a list of all your addresses.
EXAMPLE OF HOW THE FILE SHOULD LOOK address.txt:

        0x8A7c27d2cEAF29bA50f425A8e16E214c76Cff95D
        0x075948634bfb650d7145843EFFBEC1c6010a1439
        0x34523B101762CCA2145d87976D4B9ae60034B449
        IF NEEDED, ADD EACH ADDRESS ON A NEW LINE <---- Pay attention

## Next, open Windows(PowerShell)/Linux(Terminal) and navigate to the script directory.

Check the virtual environment (venv) at the beginning

Windows:

        Use the "dir" command to view the contents of the current directory.

Linux/MacOS:

        Use the "ls" or "ll" command.

EXAMPLE OF WHAT SHOULD BE:
(venv) saniksin@desktop:~/Python/withdraw_binance

## To run the program, enter:

Windows:

        python main.py

Linux/MacOS:

        python3 main.py


# ШАГ 4

## НАСТРОЙКА ПРОГРАММЫ ДЛЯ РАБОТЫ

Настраиваем API_KEY/API_SECRET в config.py либо .env. ВЫБЕРИТЕ ЧТО-ТО ОДНО!

- В API_KEY записываем ключ API.
- В API_SECRET записываем секретный ключ API.

У вас должно получится что-то на подобие:

В сonfig.py:

    API_KEY = 'jsdfhsa32-95872sdajfdsakfvh023945try72qtgsdajgvhasdsdfgjk325'
    API_SECRET = '834rdjsnfkna938457213985qdfjaskjdhfnd1208954r715r7fesdkjfnjs'

В .env:

    API_KEY=jsdfhsa32-95872sdajfdsakfvh023945try72qtgsdajgvhasdsdfgjk325
    API_SECRET=834rdjsnfkna938457213985qdfjaskjdhfnd1208954r715r7fesdkjfnjs


## Добавляем ваши адреса в address.txt.

ПРИМЕР ТОГО КАК ДОЛЖЕН ВЫГЛЯДЕТЬ ФАЙЛ address.txt:

    0x8A7c27d2cEAF29bA50f425A8e16E214c76Cff95D
    0x075948634bfb650d7145843EFFBEC1c6010a1439
    0x34523B101762CCA2145d87976D4B9ae60034B449
    ЕСЛИ НУЖНО ДОБАВЬТЕ КАЖДЫЙ АДРЕС НА НОВОЙ СТРОКЕ <---- Обратите внимание

## Далее открываем на Windows(PowerShell)/Linux(Терминал) и переходим в директории скрипта. 

Проверяем виртуальное окружение (venv) в начале

Windows:

    команда "dir" для просмотра содержимого текущей директории.

Linux/MacOS:

    команда "ls" либо "ll"

 ПРИМЕР ТОГО ЧТО ДОЛЖНО БЫТЬ:
    (venv) saniksin@desktop:~/Python/withdraw_binance

## Для запуска программы пишем:

Windows:

    python main.py

Linux/MacOS:

    python3 main.py

    
# STEP 5

# How to Use the Program

**Always preferable to withdraw through random amounts or manually specify the amount!**

To avoid detection, don't withdraw the same amount to 10 different wallets at the same second!

If unsure, make a test transaction with a small amount!

To exit at any time, press CTRL+C.

The program offers the following options:

1. Check the list of wallets for withdrawal
2. Check the status of deposits/withdrawals
3. Specify the amount for each wallet
4. Withdraw a random amount to all wallets. Difference: +1-1.5% from the specified amount
5. Withdraw the same amount of cryptocurrency to all wallets

## Check the List of Wallets for Withdrawal

- Check the list of wallets you specified in address.txt
- Enter 1

If you receive a list of your wallets (each wallet in a new line) as a response, you've done everything right!

## Check the Status of Deposits/Withdrawals

- Enter 2
- Enter the cryptocurrency ticker
- Enter the network
- If the cryptocurrency is available for withdrawal on the network, you'll see information about the minimum withdrawal amount and the fee for each withdrawal!

## Specify the Amount for Each Wallet

- Enter 3
- Enter the cryptocurrency ticker (ETH/USDT/USDC/BNB/MATIC)
- Choose the network (ETH, BSC, OPTIMISM, ARBITRUM, MATIC)
- Specify the withdrawal amount for each wallet in turn
- If everything is done correctly, the withdrawal will start automatically.
- If there's an error, try to analyze what went wrong and pay attention to the error message. You probably did something wrong!

## Withdraw a Random Amount to All Wallets

This is a fast and priority method of sending cryptocurrency to wallets. Keep in mind that an additional 1-1.5% will be added to the initially specified amount. This is done to ensure that transactions are not for the same amount!

- Enter 4
- Enter the cryptocurrency ticker (ETH/USDT/USDC/BNB/MATIC)
- Choose the network (ETH, BSC, OPTIMISM, ARBITRUM, MATIC)
- Enter the amount (a random 0 to 1.5% will be added for each wallet)
- If everything is done correctly, the withdrawal will start automatically.
- If there's an error, try to analyze what went wrong and pay attention to the error message. You probably did something wrong!

## Withdraw the Same Amount of Cryptocurrency to All Wallets

This is a less prioritized method! It's preferable not to use it, but sometimes it might be necessary!

- Enter 5
- Enter the cryptocurrency ticker (ETH/USDT/USDC/BNB/MATIC)
- Choose the network (ETH, BSC, OPTIMISM, ARBITRUM, MATIC)
- Enter the amount.
- If everything is done correctly, the withdrawal will start automatically.
- If there's an error, try to analyze what went wrong and pay attention to the error message. You probably did something wrong!

If something is unclear, it's better to ask! If unsure, it's better to send a small amount of crypto! Double-check the specified wallets! Remember, you're working with real money!


# ШАГ 5

# Как использовать программу

**Всегда желательно выводить через рандом или вручную указывать сумму!**

Чтобы не было палевно, что в одну секунду пошел вывод на 10 разных кошельков одинаковой суммы!

Если не уверены в чем-либо, сделайте тестовую транзакцию на маленькую сумму!

Для выхода в любой момент нажмите CTRL+C.

В программе доступны следующие опции:

1. Проверить список кошельков для вывода
2. Проверить статус ввода/вывода
3. Указать сумму для каждого кошелька
4. Вывести рандомную сумму на все кошельки. Разница: +1-1.5% от указанной суммы
5. Вывести одинаковое количество криптовалюты на все кошельки

## Проверить список кошельков для вывода

- Проверяем список кошельков, которые вы указали в address.txt
- Введите 1

Если в ответном сообщении вы получите список своих кошельков (каждый кошелек в новой строке), значит вы все сделали правильно!

## Проверить статус ввода/вывода

- Введите 2
- Введите тикер криптовалюты
- Введите сеть
- Если криптовалюта доступна к выводу в данной сети, вы увидите информацию о минимальной сумме вывода и комиссию за каждый вывод!

## Указать сумму для каждого кошелька

- Введите 3
- Введите тикер криптовалюты (ETH/USDT/USDC/BNB/MATIC)
- Выберите сеть (ETH, BSC, OPTIMISM, ARBITRUM, MATIC)
- По очереди укажите сумму вывода для каждого кошелька
- Если вы все сделаете правильно, автоматически начнется вывод.
- Если возникнет ошибка, попробуйте проанализировать что пошло не так, обратите внимание на ошибку. Скорее всего вы что-то сделали не так!

## Вывести рандомную сумму на все кошельки

Это быстрый и приоритетный способ отправки криптовалюты на кошельки. Учтите, что к изначально указанной сумме будет добавлено еще около 1-1.5% сверху. Это делается для того, чтобы транзакции не были на одинаковую сумму!

- Введите 4
- Введите тикер криптовалюты (ETH/USDT/USDC/BNB/MATIC)
- Выберите сеть (ETH, BSC, OPTIMISM, ARBITRUM, MATIC)
- Введите сумму (к ней будет добавлено рандомно для каждого кошелька от 0 до 1.5%)
- Если вы все сделаете правильно, автоматически начнется вывод.
- Если возникнет ошибка, попробуйте проанализировать что пошло не так, обратите внимание на ошибку. Скорее всего вы что-то сделали не так!

## Вывести одинаковое количество криптовалюты на все кошельки

Менее приоритетный способ! Желательно его не использовать! Но иногда может понадобиться!

- Введите 5
- Введите тикер криптовалюты (ETH/USDT/USDC/BNB/MATIC)
- Выберите сеть (ETH, BSC, OPTIMISM, ARBITRUM, MATIC)
- Введите сумму.
- Если вы все сделаете правильно, автоматически начнется вывод.
- Если возникнет ошибка, попробуйте проанализировать что пошло не так, обратите внимание на ошибку. Скорее всего вы что-то сделали не так!

Если вам что-то не понятно - лучше спросите! Если не уверены - лучше отправьте маленькое количество крипты! Перепроверяйте указанные кошельки! Помните, что вы работаете с реальными деньгами!

