Задание
Написать REST микросервис на языке python с применением фремфорка FastAPI

База данных: PostgreSQL
ORM: SQLAlchemy
Валидаторы данных (схемы) - Pydantic

Функциональность:
1. POST /tasks/add добавляет задачу в базу данных
{
"task_uuid": "UUID",
"description": "тестовая задача",
"params": {
"param_1": "1",
"param_2": 1
}
}
2. GET /tasks - получает все существующие задачи
3. PUT /tasks/<task_sid> - обновляет задачу по sid
