## Service

### Описание проекта
Данное приложение было разработано в рамках тестового задания:
```
Сервис определения информации по имени
Нужно реализовать программу, которая по введенному имени должна выводить возраст, пол и
национальность. Сервис должен обращаться по API к нескольким сервисам (перечень ниже).
В качестве интерфейса использовать CLI (command line interface).

Бонусная часть 
Необходимо реализовать возможность кеширования значений в БД SQLite. В БД необходимо
хранить запрос (имя), результаты (пол, возраст, национальность), а также время и дату
запроса, и полученные ответы от API.
Список сервисов, к которым необходимо обращаться:
- https://agify.io/
- https://genderize.io/
- https://nationalize.io/

```

### Технологии
- Python 3.9
- aiohttp
- Sqlite

### Запуск проекта

1. Склонировать репозиторий:

```
git clone git@github.com:verafadeeva/test-service.git
```
2. Перейти папку с проектом:
```
cd test-service
```
3. Для управления зависимостями в проекте используется [poetry](https://python-poetry.org/docs/).
4. В директории /test-blog выполнить команду:
```
make
```
5. После установки зависимостей и активации окружения, для инициализации бд выполнить:
```
make initial
```

### Пример использования
```
$ python main.py <Name>
```
Ответ:
```
{
    "name": "John",
    "age": 72,
    "gender": "male",
    "nationality": "IE",
    "created_at": "2023-11-24T12:00:02.510550"
}
```

### Автор
- Вера Фадеева ([@fadeevavera](https://t.me/fadeevavera))