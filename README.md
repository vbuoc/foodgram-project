# Cайт «Продуктовый помощник»
![example workflow](https://github.com/vbuoc/foodgram-project/actions/workflows/main.yml/badge.svg)

Это онлайн-сервис, где пользователи смогут публиковать рецепты, подписываться 
на публикации других пользователей, добавлять понравившиеся рецепты в список 
«Избранное», а перед походом в магазин скачивать сводный список продуктов, 
необходимых для приготовления одного или нескольких выбранных блюд. Список покупок доступен
любому пользователю, в том числе и не авторизованному.

Вы можете протестировать проект: http://84.252.140.86

# Стек технологий
Проект написан на Python с использованием веб-фреймворка Django.
- используется Django Rest Framework для обработки запросов от JS;
- используется база данных PostgreSQL;
- Gunicorn + Nginx;
- CI/CD: Docker, docker-compose, GitHub Actions;
- Проект развернут на Yandex.Cloud;
- работа с изображениями - django-stdimage

## Установка
- Клонируйте проект
    ```bash
    git clone git@github.com:vbuoc/foodgram-project.git
    ```
- Перейдите в директорию проекта
    ```bash
    cd foodgram-project/
    ```
- переименуйте файл ```.env.template``` в ```.env```

- Выполните docker-compose
    ```bash
    docker-compose -f docker-compose.yaml up -d
    ```
- Загрузите тестовые данные
    ```bash
    docker-compose -f docker-compose.yaml run --rm web python manage.py loaddata fixtures.json
    ```  
- Создайте суперпользователя
    ```bash
    docker-compose -f docker-compose.yaml run --rm web python manage.py createsuperuser
    ```
  
## Также
Вы можете загрузить список ингредиентов в пустую базу через команду 

```bash
docker-compose -f docker-compose.yaml run --rm web python manage.py load_ingredients
```
либо воспользоваться "админкой" сайта и загрузить ингредиенты, используя технологию:
`django-import-export
`
## Автор
По вопросам сотрудничества или просто по любым вопросам вы можете написать мне:

<a href="mailto:rus.buoc@gmail.com?"><img src="https://img.shields.io/badge/gmail-%23DD0031.svg?&style=for-the-badge&logo=gmail&logoColor=white"/></a>

