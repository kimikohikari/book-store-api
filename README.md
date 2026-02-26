# 📚 Book Store API

<p align="center">
  <b>FastAPI backend project with JWT authentication and role-based access</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg">
  <img src="https://img.shields.io/badge/FastAPI-0.110+-teal.svg">
  <img src="https://img.shields.io/badge/PostgreSQL-DB-blue.svg">
  <img src="https://img.shields.io/badge/JWT-Auth-green.svg">
</p>

 (EN) About Project

**Book Store API** is a backend application for managing a bookstore, written in **FastAPI**.
The project implements a full-fledged authentication, authorization, and database management system.

The project was created **as a portfolio project for the Junior Python Backend Developer position**.

---

## 🚀 Tech Stack

- 🐍 **Python 3**
- ⚡ **FastAPI**
- 🗄 **PostgreSQL**
- 🔐 **JWT Authentication**
- 🔑 **Passlib (bcrypt)**
- 🧠 **SQLAlchemy ORM**
- 🌐 **Uvicorn**

---

## 🔐 Functionality

### 👤 Authentication
- User Registration
- Authorization (JWT Token)
- Password Hashing
- Role Model (user / admin)

### 📚 Books
- ➕ Create a Book *(admin only)*
- 📄 Get a List of Books
- 🔍 Get a Book by ID
- ✏️ Update a book *(admin only)*
- ❌ Delete a book *(admin only)*

---

## 🗂 Project Structure
```bash
app/
├── api/ # Routers
│ ├── auth.py
│ ├── books.py
│ └── deps.py
├── core/ # Security and Settings
│ └── security.py
├── crud/ # Database Logic
├── models/ # SQLAlchemy Models
├── schemas/ # Pydantic Schemas
├── database.py # Database Connection
└── main.py # Entry Point
```

---

## ⚙️ Installation and Run

### 1️⃣ Cloning the Repository

```bash
git clone https://github.com/kimikohikari/book-store-api.git
cd book-store-api
```

### 2️⃣ Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```
### 3️⃣ Installing Dependencies

```bash
pip install -r requirements.txt
```
### 4️⃣ Environment Variables

Create a file .env:
```bash
DATABASE_URL=postgresql://user:password@localhost:5432/bookstore
SECRET_KEY=your_secret_key
```
### 5️⃣ Launching the Application

```bash
uvicorn app.main:app --reload
```
---

📌 API Documentation

Swagger UI is available at:
```bash
http://127.0.0.1:8000/docs
```
---

---

## (RU) О проекте

**Book Store API** — это backend-приложение для управления книжным магазином, написанное на **FastAPI**.  
Проект реализует полноценную систему аутентификации, авторизации и работу с базой данных.

Проект создавался **как портфолио-проект для позиции Junior Python Backend Developer**.

---

## 🚀 Стек технологий

- 🐍 **Python 3**
- ⚡ **FastAPI**
- 🗄 **PostgreSQL**
- 🔐 **JWT Authentication**
- 🔑 **Passlib (bcrypt)**
- 🧠 **SQLAlchemy ORM**
- 🌐 **Uvicorn**

---

## 🔐 Функциональность

### 👤 Аутентификация
- Регистрация пользователя
- Авторизация (JWT токен)
- Хеширование паролей
- Ролевая модель (user / admin)

### 📚 Книги
- ➕ Создание книги *(admin only)*
- 📄 Получение списка книг
- 🔍 Получение книги по ID
- ✏️ Обновление книги *(admin only)*
- ❌ Удаление книги *(admin only)*

---

## 🗂 Структура проекта
```bash
app/
├── api/ # Роутеры
│ ├── auth.py
│ ├── books.py
│ └── deps.py
├── core/ # Безопасность и настройки
│ └── security.py
├── crud/ # Логика работы с БД
├── models/ # SQLAlchemy модели
├── schemas/ # Pydantic схемы
├── database.py # Подключение к БД
└── main.py # Точка входа
```


---

## ⚙️ Установка и запуск

### 1️⃣ Клонирование репозитория

```bash
git clone https://github.com/kimikohikari/book-store-api.git
cd book-store-api
```

### 2️⃣ Виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate
```
### 3️⃣ Установка зависимостей

```bash
pip install -r requirements.txt
```
### 4️⃣ Переменные окружения

Создайте файл .env:
```bash
DATABASE_URL=postgresql://user:password@localhost:5432/bookstore
SECRET_KEY=your_secret_key
```
### 5️⃣ Запуск приложения

```bash
uvicorn app.main:app --reload
```
---

📌 Документация API

Swagger UI доступен по адресу:
```bash
http://127.0.0.1:8000/docs
```


