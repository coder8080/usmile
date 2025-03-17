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
    "ok-link": "Количество сертификатов у вас: {%COUNT%}"
}
