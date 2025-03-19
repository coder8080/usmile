<a href="https://usmileclinic.ru/">
    <img src="./media/site_logo.jpg" alt="Usmile logo" title="Usmile" align="right" height="60" />
</a>

# USMILE Telegram Bot

<p align="center">
    <a href="https://t.me/usmile_cert_bot">
        <img alt="telegram-bot" src="./media/bot_logo_small.png">
    </a>
</p>

Телеграм бот для создания партнерских сертификатов стоматологии usmile

## Техническая информация

### Стек

- [Python3](https://www.python.org/)
- [Aiogram3](https://aiogram.dev/)
- [Peewee](https://github.com/coleifer/peewee)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [PostgreSQL](https://www.postgresql.org/)

### Запуск

#### Продакшен

```bash
docker compose --profile prod up --build -d
```

#### Разработка

```bash
docker compose --profile dev up --build
```
