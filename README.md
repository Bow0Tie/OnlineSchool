# OnlineSchool / Система для обучения
Simple architecture and API for OnlineSchool needs / Простая архитектура и API для системы обучения.

Simple architecture and API implemented as a test task for training purposes.

Простая архитектура и API реализованные в качестве тестового задания в целях обучения.


## Tables Screenshots / Скриншоты таблиц

### Entries in the User table / Записи в таблице User

![alt text](https://github.com/Bow0Tie/OnlineSchool/blob/main/examples/users_table.png?raw=true)

### Entries in the Product table / Записи в таблице Product

![alt text](https://github.com/Bow0Tie/OnlineSchool/blob/main/examples/products_table.png?raw=true)

### Entries in the Tutorial table / Записи в таблице Tutorial

![alt text](https://github.com/Bow0Tie/OnlineSchool/blob/main/examples/Tutorials_table.png?raw=true)

### Entries in the UserTutorial table / Записи в таблице UserTutorial

![alt text](https://github.com/Bow0Tie/OnlineSchool/blob/main/examples/UserTutorials_table.png?raw=true)

## Requests examples / Примеры запросов

Requests exported from Postman / Экспорт запросов из постмана [file](https://github.com/Bow0Tie/OnlineSchool/blob/main/examples/all%20requests%20collection.json)

## Responses examples / Примеры ответов

### User get all tutorials by products / Получение пользователем статистики по всем урокам по всме продуктам

user_id = 7

```json

{
    "Cats": [
        {
            "Cat1": [
                0,
                false
            ]
        },
        {
            "Cat2": [
                0,
                false
            ]
        },
        {
            "Cat3": [
                0,
                false
            ]
        }
    ],
    "Cats and Dogs": [
        {
            "Cat1": [
                0,
                false
            ]
        },
        {
            "Cat3": [
                0,
                false
            ]
        },
        {
            "Dog1": [
                0,
                false
            ]
        },
        {
            "Dog3": [
                800,
                true
            ]
        }
    ]
}

```

File [link](https://github.com/Bow0Tie/OnlineSchool/blob/main/examples/user%20get%20all%20tutorials%20by%20products%20user_id%207.json) / Ссылка на [файл](https://github.com/Bow0Tie/OnlineSchool/blob/main/examples/user%20get%20all%20tutorials%20by%20products%20user_id%207.json)

### User get all tutorials by specific product / Получение пользователем статистики по всем урокам по конкретному продукту

user_id = 7
product_id = 8

```json

{
    "Cats and Dogs": [
        {
            "Cat1": [
                0,
                false,
                "2023-09-23T11:47:23.696Z"
            ]
        },
        {
            "Cat3": [
                0,
                false,
                "2023-09-23T11:47:23.696Z"
            ]
        },
        {
            "Dog1": [
                0,
                false,
                "2023-09-23T11:47:23.696Z"
            ]
        },
        {
            "Dog3": [
                800,
                true,
                "2023-09-23T11:48:07.048Z"
            ]
        }
    ]
}

```

File [link](https://github.com/Bow0Tie/OnlineSchool/blob/main/examples/user%20get%20all%20tutorials%20by%20specific%20product%20user_id%207%20product_id%208.json) / Ссылка на [файл](https://github.com/Bow0Tie/OnlineSchool/blob/main/examples/user%20get%20all%20tutorials%20by%20specific%20product%20user_id%207%20product_id%208.json)

### Get statistic by all products / Получение статистики по всем урокам по всем продуктам на платформе

```json

{
    "Cats": {
        "Total watches": 0,
        "Total watch time": null,
        "Total students": 2,
        "Conversion": "40 %"
    },
    "Dogs": {
        "Total watches": 1,
        "Total watch time": 800,
        "Total students": 2,
        "Conversion": "40 %"
    },
    "Cats and Dogs": {
        "Total watches": 1,
        "Total watch time": 800,
        "Total students": 1,
        "Conversion": "20 %"
    }
}

```

File [link](https://github.com/Bow0Tie/OnlineSchool/blob/main/examples/get%20statistic%20by%20all%20products.json) / Ссылка на [файл](https://github.com/Bow0Tie/OnlineSchool/blob/main/examples/user%20get%20all%20tutorials%20by%20specific%20product%20user_id%207%20product_id%208.json)
