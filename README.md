# Тестовое задание с использование Django + Stripe API

Проект загружен на хостинг PythonAnywhere - https://altyofficial.pythonanywhere.com/item/1/
К проекту написана тестовая база данных. Подробнее об этом в шагах запуска проекта. Так как это тестовый функционал stripe, номер карты должен быть тоже тестовым - 4242 4242 4242 4242

<hr>

## Проект можно запустить в двух вариантах: на локальном сервере и в Docker контейнерах.

- [Запуск проекта локально](#установка-проекта-локально)
- [Запуск проекта в Docker контейнерах](#установка-проекта-в-docker-контейнерах)

<hr>

### При необходимости нужно изменить файл ```.env``` в директории /project/ 
В этом проекте я запушил этот файл на гитхаб для просмотра всего функционала.

#### Шаблон наполнения env-файла (кавычки убрать)
```sh
DJANGO_SECRET_KEY=<СЕКРЕТНЫЙ КЛЮЧ ДЖАНГО>
STRIPE_PUBLIC_KEY=<ПУБЛИЧНЫЙ КЛЮЧ STRIPE>
STRIPE_SECRET_KEY=<СЕКРЕТНЫЙ КЛЮЧ STRIPE>
```

<hr>

## Интсрументы и технологии
![](https://img.shields.io/badge/python-3.11-blue)
![](https://img.shields.io/badge/django-4.1.7-yellowgreen)
![](https://img.shields.io/badge/gunicorn-20.1-%20%2320bdb0)
![](https://img.shields.io/badge/stripe-5.1.1-green)
![](https://img.shields.io/badge/docker-20.10.22-%20%232a37a3)
![](https://img.shields.io/badge/nginx-1.23.3-%20%23a17828)

<hr>
<br>

## Установка проекта локально 
#### Клонировать проект
```sh
https://github.com/AltyOfficial/test_stripe.git
```
#### Создать и установить виртуальное окружение, установить зависимости
```sh
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
#### Перейти в директорию с manage.py, выполнить миграции и загрузить данные в базу, запустить веб-сервер
```sh
cd project/stripe_api/
python manage.py makemigrations
python manage.py migrate
python manage.py load_data
python manage.py runserver
```

#### Проект будет доступен по адресу http://127.0.0.1:8000/ и http://localhost:8000/

<hr>

## Установка проекта в Docker контейнерах

#### В окне терминала из корневой директории выполнить команды для запуска контейнеров
```sh
docker-compose up -d --build
```
- Команда ```-d``` нужна для фоновой работы контейнера
- Файлы конфигурации описаны в ```/nginx.conf``` и ```/docker-compose.yml```, при необходимости изменить

#### После запуска контейнеров выполнить команды миграции, сбора статики и загрузки данных в базу
```sh
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --no-input
docker-compose exec web python manage.py load_data
```
#### Для создания суперпользователя выполнить команду
```sh
docker-compose exec web python manage.py createsuperuser
```

#### Проект будет доступен по адресу http://127.0.0.1/