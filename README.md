# HTTPX + Pydantic API Tests

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-9.x-orange)](https://docs.pytest.org/)
[![HTTPX](https://img.shields.io/badge/HTTPX-0.28.x-purple)](https://www.python-httpx.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.x-red)](https://docs.pydantic.dev/)
[![Allure](https://img.shields.io/badge/Allure-Report-yellow)](https://docs.qameta.io/allure/)

Автоматизированные тесты REST API на стеке **HTTPX + Pydantic + Pytest + Allure**. Проект демонстрирует валидацию контрактов, позитивные и негативные сценарии, фикстуры и CI/CD.

---

## Тестируемое API

Локальное API: [qa-automation-engineer-api-course](https://github.com/Nikita-Filonov/qa-automation-engineer-api-course)

---

## Покрытие тестами

### Эндпоинты
- **GET** — получение сущностей
- **POST** — создание сущностей
- **PATCH** — обновление сущностей
- **DELETE** — удаление сущностей

### Типы сценариев
- Позитивные: CRUD-операции с валидными данными
- Негативные: валидация ошибок (некорректные данные, несуществующие ID)

---

## Используемые технологии

- **HTTPX** — HTTP-клиент для тестирования REST API
- **Pydantic** — валидация контрактов (модели для каждого эндпоинта + отдельные модели для ошибок в негативных тестах)
- **Faker** — генерация тестовых данных внутри Pydantic-моделей
- **Фикстуры** — для разных эндпоинтов; подключаются через `conftest.py` как плагины
- **Allure Report** — отчёты с шагами и логированием
- **CI/CD** — GitHub Actions с автозапуском по коммиту

---

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/DmitriyChernakov/autotests-ui.git
cd autotests-ui
```

### 2. Установить зависимости

```bash
pip install -r requirements.txt
playwright install --with-deps
```

### 3. Запустить API

Инструкция в репозитории API: [qa-automation-engineer-api-course](https://github.com/Nikita-Filonov/qa-automation-engineer-api-course)

### 4. Запустить тесты

```bash
pytest -m regression --alluredir=allure-results
```

### 5. Просмотреть Allure-отчёт

```bash
allure serve ./allure-results
```

**Примечание:** Allure должен быть установлен локально. Инструкция по установке: [Allure](https://allurereport.org/docs/)
