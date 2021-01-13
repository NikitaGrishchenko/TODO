# DJANGO & VUE TEMPLATE

```
make install – установка всех зависимостей
make run – запуск серверов
make createadmin – создание админа
make migrate – миграции

python3 -m venv .venv – создание виртуального окружения Linux
source .venv/bin/activate – активация виртуального окружения Linux

python -m venv .venv – создание виртуального окружения Windows
source .venv/Scripts/activate – активация виртуального окружения Windows

pip freeze – вывести установленные модули в консоль
pip freeze > requirements.txt – сохранить установленные модули в файл

pip install -r requirements.txt – установка зависимостей из requirements.txt
yarn – установк зависимостей для frontend

yarn serve – старт сервера Vue
python ./backend/manage.py runserver – старт сервера Django

python ./backend/manage.py makemigrations – применить миграции
python ./backend/manage.py migrate – выполнить миграции

Создание приложения example
1. создать папку example в backend/apps
2. cd backend
3. django-admin startapp example apps/example
```

# TASKS

```
[x]1. Добавить шрифт Roboto
[x]2. Добавить дату выполнения задачи (дедлайн)
[x]3. Копки удалить и редактировать появляются лишь при наведении на определенную задачу
[x]4. Добавить приоритет задачам в виде воск. знаков или флажком или border
[x]5. Исправить косяк со временем
[ ]6. Избавиться от editing в БД
[x]7. Изменить форму добавления, добавить возможность выбора дедлайна и приоритета
[ ]8. Выводить приоритеты из API
  [ ]8.1 Компонент "select приоритет"
[x]9. Расширить админку
[x]10. Регистрация
  [x]10.1 Валидация пароля
  [x]10.2 Вывод на login.html информацию об успешной регистрации
  [x]10.3 Вывод ошибок на signup.html
  [x]10.4 Залочить использование кириллицы в пароле
  [x]10.5 Валидация мыла
  [x]10.6 Установить ограничение на загружаемое фото
[x]11. Решить проблему с виджетом "Задач нет"
[x]12. Подтверждение выхода
[x]13. Заглушка "Ошибка, вы уже авторизированы"



```
