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

## Responses examples / Примеры ответов

### Получение пользователем статистики по всем урокам по всме продуктам

user_id = 7

```json

{"Cats": [{"Cat1": [0, false]}, {"Cat2": [0, false]}, {"Cat3": [0, false]}], "Cats and Dogs": [{"Cat1": [0, false]}, {"Cat3": [0, false]}, {"Dog1": [0, false]}, {"Dog3": [800, true]}]}

```

