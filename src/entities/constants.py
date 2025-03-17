from os import getenv

TOKEN = getenv("TOKEN")
POSTGRES_USER = getenv("POSTGRES_USER")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD")
ADMINS = list(map(int, getenv("ADMINS").split(',')))

TEXT = {
    "simple-user-start": "Пожалуйста, воспользуйтесь ссылкой от \
сотрудника usmile или добавьте свой id в список администраторов: \
<code>{%ID%}</code>",
    "admin-start": "Вы администратор бота и можете выписывать сертификаты.",
    "wrong-link": "Неверная ссылка",
    "used-link": "Ссылка уже использована",
    "ok-link": "Количество сертификатов у вас: {%COUNT%}",
    "create-link": "➕ Создать новую ссылку",
    "input-count": "Отправьте одно число: количество сертификатов",
    "link-created": "Вот ваша ссылка (нажмите, чтобы скопировать): \
<code>{%LINK%}</code>",
    "unknown-message": "🥲 Я вас не понял\n/start - перезапустить бота",
    "create-cert": "📄 Выпустить новый сертификат",
    "input-names": "Напишите имя, на которое нужно выпустить сертификат. \
Вы можете написать в столбик несколько имен"
}
