<a href="https://usmileclinic.ru/">
    <img src="./media/site_logo.jpg" alt="Usmile logo" title="Usmile" align="right" height="60" />
</a>

# 🦷 USMILE Telegram Bot

<p align="center">
    <a href="https://t.me/usmile_cert_bot">
        <img alt="telegram-bot" src="./media/bot_logo_small.png">
    </a>
</p>

<div align="center">

<a href="#">![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)</a>
<a href="#">![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)</a>
<a href="#">![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)</a>
<a href="#">![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)</a>
<a href="#">![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)</a>

</div>

Телеграм бот для создания партнерских сертификатов стоматологии usmile

⭐️ Поставьте звездочку - это очень мотивирует)

## Функции

- Администраторы могут создавать особые ссылки для партнеров
- Пройдя по ссылке, партнер пополняет свой баланс
- Партнер может создавать сертификаты, используя свой баланс
- Администраторы могут проверить статус сертификата по его номеру
- Администраторы могут пометить сертификат как использованный

## Техническая информация

### Стек

- [Python3](https://www.python.org/)
- [Aiogram3](https://aiogram.dev/) - библиотека для создания телеграм-ботов
- [Peewee](https://github.com/coleifer/peewee) - легковесная ORM
- [Docker](https://www.docker.com/) - контейнеризация
- [Docker Compose](https://docs.docker.com/compose/) - удобный запуск нескольких контейнеров
- [PostgreSQL](https://www.postgresql.org/) - база данных
- [Redis](https://redis.io/) - быстрое хранилище типа ключ-значение

### Разработка

#### Установка зависимостей

Зависимости устанавливаются во время сборки Docker контейнера. Но чтобы в вашем редакторе кода работало автодополнение, рекомендуется также установить зависимости в виртуальную среду:

```bash
python3 -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```

#### Запуск

```bash
docker compose --profile dev up --build
```

- `--profile dev` - использует параметры docker для разработки
- `up` - запускает проект
- `--build` - пересобирает контейнеры

При внесении изменений в файлы на диске бот перепускается. Реализовано с помощью [volumes](https://docs.docker.com/engine/storage/volumes/) и [watchdog](https://pypi.org/project/watchdog/)

#### Добавление новых пакетов

Все пакеты, использующиеся проектом (даже во время разработки) должны быть добавлены в `requirements.txt`

Команды ниже предполагают, чтовы уже [установили зависимости](#установка-зависимостей)

```bash
pip install package # package - ваш пакет
pip freeze > requirements.txt # обновляет requirements.txt
```

### Продакшен

_Сборка и деплой автоматизированы с помощью [github-actions](https://github.com/coder8080/usmile/actions)_

**Команда запуска**

```bash
docker compose --profile prod up -d
```

- `--profile prod` - использует параметры docker для продакшена
- `up` - запускает проект
- `-d` - фоновый режим и запуск при загрузке системы
