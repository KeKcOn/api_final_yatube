# api_final

## Описание

Этот проект представляет собой API, где пользователи могут создавать посты,
комментировать их, подписываться на других пользователей. Проект разработан с
использованием Django и Django REST framework.

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
    python3 -m venv venv
    ```
    ```bash
    . venv/bin/activate
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

Теперь ваш проект api_final должен быть доступен по
адресу http://localhost:8000/.

## Примеры запросов к API

1. Создание нового поста:

   ```bash
   POST /api/v1/posts/
   {
      "text": "Заголовок поста",
   }
   ```
2. Создание комментария к посту:

   ```bash
   POST /api/v1/posts/{post_id}/comments/
   {
      "text": "Текст комментария"
   }
   ```
3. Подписка на другого пользователя:

    ```bash
   POST /api/v1/follow/
   {
      "following": "имя_пользователя"
   }
    ```
4. Получение списка постов по группе:
   
   ```bash
   GET /api/v1/groups/{id}/
   ```
5. Получение списка пользователей, на которых подписан текущий пользователь:

   ```bash
   GET /api/v1/follow/
   ```