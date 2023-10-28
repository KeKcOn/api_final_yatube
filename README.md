# api_final


## Как запустить проект

1. Клонировать репозиторий и перейти в него в командной строке:

    ```bash
    git clone git@github.com:KeKcOn/api_final_yatube.git
    ```

    ```bash
    cd api_final_yatube
    ```
2. Создать и активировать виртуальное окружение:

    ```bash
    python3 -m venv env
    ```
    ```bash
    source env/bin/activate
    ```
3. Установить зависимости из файла requirements.txt:

    ```bash
    python3 -m pip install --upgrade pip
    ```
    ```bash
    pip install -r requirements.txt
    ```
4. Выполнить миграции:

   ```bash
   python3 manage.py migrate
   ```
6. Запустить проект:

   ```bash
   python3 manage.py runserver
   ```

Теперь ваш проект api_final должен быть доступен по адресу http://localhost:8000/.
