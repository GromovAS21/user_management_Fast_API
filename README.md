# User Management API

Это API для управления пользователями. Оно позволяет получать список пользователей, получать информацию о конкретном пользователе, создавать новых пользователей и удалять существующих.

## Основные маршруты

### 1. Получение списка пользователей

**Метод:** `GET`

**URL:** `/users/`

**Описание:** Возвращает список всех пользователей.

**Пример ответа:**

```json
[
    {
        "id": 1,
        "name": "John",
        "age": 25,
        "email": "john@example.com"
    },
    {
        "id": 2,
        "name": "Jane",
        "age": 26,
        "email": "jane@example.com"
    }
]
```

### 2. Получение пользователя по ID
**Метод:** `GET`

**URL:** `/users/{user_id}`

**Описание:** Возвращает информацию о пользователе по его ID.

**Параметры:**

**user_id (int):** ID пользователя.

**Пример ответа:**

```json
{
    "id": 1,
    "name": "John",
    "age": 25,
    "email": "john@example.com"
}
```

**Ошибки:**

**404 Not Found:** User not found

### 3. Создание нового пользователя
**Метод:** `POST`

**URL:** `/users/`

**Описание:** Создает нового пользователя.

**Тело запроса:**

```json
{
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
}
```
**Пример ответа:**

```json
{
    "id": 3,
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
}
```
**Ошибки:**

**400 Bad Request:** User already exists

### 4. Удаление пользователя по ID
**Метод:** `DELETE`

**URL:** `/users/{user_id}`

**Описание:** Удаляет пользователя по его ID.

**Параметры:**

**user_id (int):** ID пользователя.

**Пример ответа:**

```json
{
    "message": "User deleted"
}
```
**Ошибки:**

**404 Not Found:** User not found

### Модели данных

**Пользователь (User)**

```json
{
    "id": 1,
    "name": "John",
    "age": 25,
    "email": "john@example.com"
}
```
**Создание пользователя (UserCreate)**

```json
{
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
}
```
### Примеры использования
**1. Получение списка пользователей**

```bash
curl -X GET "http://localhost:8000/users/"
```

**2. Получение пользователя по ID**

```bash
curl -X GET "http://localhost:8000/users/1"
```
**3. Создание нового пользователя**
```bash
curl -X POST "http://localhost:8000/users/" 
-H "Content-Type: application/json" 
-d '{"name": "Alice", "age": 30, "email": "alice@example.com"}'
```

**4. Удаление пользователя по ID**
```bash
curl -X DELETE "http://localhost:8000/users/1"
```

### Запуск приложения

**Для запуска приложения используйте команды:**

```bash
git clone https://github.com/GromovAS21/user_management_Fast_API.git
cd user_management_Fast_API
poetry install 
poetry shell
uvicorn main:app --reload
```

Приложение будет доступно по адресу http://localhost:8000.

Эта документация охватывает все основные аспекты вашего API, включая маршруты, модели данных, примеры использования и инструкции по запуску.