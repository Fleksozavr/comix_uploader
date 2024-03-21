# comix_uploader
Загрузка комиксов в телеграм канал. Данный скрипт вам поможет выклдывать комиксы с сайта [xkcd.com](https://xkcd.com/353/) в ваш телеграм канал.

## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
- [Contributing](#contributing)
- [To do](#to-do)
- [Команда проекта](#команда-проекта)

## Технологии
- [Python]([https://www.gatsbyjs.com/](https://www.python.org/))
- [Telegram]([https://www.typescriptlang.org/](https://web.telegram.org/))
- [Aiogram](https://aiogram.dev/)

## Использование
Python3 должен быть уже установлен. Затем используйте pip (или pip3, если есть конфликт с Python2) для дальнейшей установки зависимостей:

### Настройка .env
Добавьте в .env переменные для дальнейшей работы:
```sh
BOT_TOKEN=ТОКЕН БОТА
CHAT_ID=ЧАТ АЙДИ КАНАЛА
```

### Требования
Для установки и запуска проекта, необходим [Python](https://python.org/) 3.

### Установка зависимостей
Для установки зависимостей, выполните команду:
```sh
pip install -r requirements.txt
```

### Запуск Development сервера
Чтобы запустить телеграм бота выполните команду (pip должен быть уже установлен):
```sh
python bot.py
```

## Contributing
Как помочь в разработке проекта? Как отправить предложение или баг-репорт. Как отправить доработку (оформить pull request, какие стайлгайды используются). Можно вынести в отдельный файл — [Contributing.md](./CONTRIBUTING.md).

## FAQ 

### Зачем вы разработали этот проект?
Чтобы был.

## To do
- [x] Добавить начальный функционал бота
- [ ] Добавить больше функций

## Команда проекта
Оставьте пользователям контакты и инструкции, как связаться с командой разработки.

- [Михаил](https://t.me/Fleksozavr) — Back-end Engineer

## Источники
Идея проекта была взята с [dvmn.org](https://dvmn.org/modules/web-api/lesson/xkcd/#1)
