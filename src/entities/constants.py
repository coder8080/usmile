from os import getenv
from typing import cast

TOKEN = cast(str, getenv("TOKEN"))
assert TOKEN

POSTGRES_USER = getenv("POSTGRES_USER")
assert POSTGRES_USER

POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD")
assert POSTGRES_PASSWORD

POSTGRES_HOST = getenv("POSTGRES_HOST")
assert POSTGRES_HOST

POSTGRES_PORT_STR = getenv("POSTGRES_PORT")
assert POSTGRES_PORT_STR
POSTGRES_PORT = int(POSTGRES_PORT_STR)

REDIS_HOST = getenv("REDIS_HOST")
assert REDIS_HOST

ADMINS = list(map(int, (getenv("ADMINS") or "").split(",")))
BOT_NAME = getenv("BOT_NAME")

TEXT = {
    "simple-user-start": "Пожалуйста, воспользуйтесь ссылкой от \
сотрудника usmile или добавьте свой id в список администраторов: \
<code>{%ID%}</code>",
    "admin-start": "Вы администратор бота и можете выписывать сертификаты.",
    "wrong-link": "Неверная ссылка",
    "used-link": "Ссылка уже использована",
    "ok-link": "Количество сертификатов у вас: {%COUNT%}",
    "create-link": "➕ Создать новую ссылку",
    "input-count": "Отправьте одно число: количество сертификатов или \
/cancel, чтобы отменить",
    "link-created": "Вот ваша ссылка (нажмите, чтобы скопировать): \
<code>{%LINK%}</code>",
    "unknown-message": "🥲 Я вас не понял\n/start - перезапустить бота",
    "create-cert": "📄 Выпустить новый сертификат",
    "input-name": "Напишите имя, на которое нужно выпустить сертификат. \
Вы можете написать в столбик несколько имен. /cancel, чтобы отменить",
    "not-enough-count": "Вам не выдано достаточно сертификатов, чтобы \
выписать их на каждого из этих людей",
    "certs-ready": "Все сертификаты сгенерированы успешно",
    "error": "🥲 Произошла непредвиденная ошибка. Мы уже знаем о проблеме \
и решаем ее",
    "check-cert": "❓ Проверить сертификат",
    "input-cert": "Отправьте номер сертификата. /cancel, чтобы отменить",
    "no-cert": "Сертификата с таким номером не существует.",
    "used-cert": "Этот сертификат уже был использован.",
    "ok-cert": "✅ Сертификат был создан на имя {%NAME%} и еще не был \
использован",
    "input-used": "Пометить сертификат как использованный?",
    "ok-used": "Сертификат помечен как использованный",
    "ok-unused": "Сертификат не был помечен как использованный",
    "credits": "Built with ❤️ by [coder8080](https://github.com/coder8080) \
and [danosito](https://github.com/danosito)",
    "check-count": "🧮 Проверить количество сертификатов",
    "admin-count": "Вы являетесь администратором и можете создавать \
сколько угодно сертификатов",
    "user-count": "У вас осталось сертификатов: {%COUNT%}",
    "cancel": "❌ Отмена",
    "create-link-cancelled": "👌 Создание ссылки отменено",
    "create-cert-cancelled": "👌 Создание сертификата отменено",
    "check-cert-cancelled": "👌 Проверка сертификата отменена",
    "start-create-cert": "Генерирую сертификаты. Это может занять ⏱️ некоторое время. Пожалуйста, подождите...",
}
