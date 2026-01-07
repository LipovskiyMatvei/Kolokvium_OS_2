# Kolokvium_OS_2
Вот полный текст для файла README.md одним куском. Просто скопируй и вставь.

code
Markdown
download
content_copy
expand_less
# To-Do List API (Flask)

Простой REST API для управления списком задач, написанный на Python с использованием микрофреймворка Flask.
Проект реализует полный набор CRUD-операций (Create, Read, Update, Delete) и хранит данные в оперативной памяти (In-Memory).

## Технологии

- **Язык:** Python 3
- **Фреймворк:** Flask
- **Формат данных:** JSON

## Установка и запуск

1. **Клонируйте репозиторий** (или скачайте файлы):
   ```bash
   git clone <LipovskiyMatvei/Kolokvium_OS_2>

Установите зависимости:
В проекте используется файл requirements.txt.

code
Bash
download
content_copy
expand_less
pip install -r requirements.txt

(Если файла нет, просто выполните: pip install flask)

Запустите сервер:

code
Bash
download
content_copy
expand_less
python app.py

После запуска API будет доступен по адресу: http://127.0.0.1:5000

Документация API
1. Получить список всех задач

URL: /tasks

Метод: GET

Ответ (200 OK):

code
JSON
download
content_copy
expand_less
[
  {
    "id": 1,
    "title": "Пример задачи",
    "description": "Описание...",
    "status": "todo"
  }
]
2. Создать новую задачу

URL: /tasks

Метод: POST

Тело запроса (JSON):

code
JSON
download
content_copy
expand_less
{
  "title": "Название задачи", 
  "description": "Описание задачи (необязательно)"
}

Валидация: Поле title является обязательным, должно быть строкой и не может быть пустым.

Ответ (201 Created): Возвращает созданный объект с ID.

3. Получить задачу по ID

URL: /tasks/<id>

Метод: GET

Пример: /tasks/1

Ответ: Объект задачи или ошибка 404 Not Found, если ID не найден.

4. Обновить задачу

URL: /tasks/<id>

Метод: PUT

Тело запроса (JSON):
Можно передать любые поля, которые нужно изменить.

code
JSON
download
content_copy
expand_less
{
  "title": "Новое название",
  "status": "done"
}

Допустимые статусы: "to do", "done", "is_requiered".

Ответ (200 OK): Возвращает обновленную задачу.

5. Удалить задачу

URL: /tasks/<id>

Метод: DELETE

Ответ (200 OK): {"result": true}

Проект разработан в рамках учебного задания.

code
Code
download
content_copy
expand_less
