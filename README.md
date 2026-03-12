# Django Blog Application
A full-featured blog platform built with Django, featuring user authentication, profile management, and a robust posting system.
## 🚀 Getting Started
### Prerequisites
- Python 3.12+
- Virtual Environment (recommended)
### Installation & Setup
1. **Clone the repository:**
     git clone <your-repo-url>
     cd django-venv/django_project
2. **Create and activate a virtual environment:**

On Linux/macOS
    ```python3 -m venv venv
    source venv/bin/activate```


On Windows
    ```python -m venv venv
     .\venv\Scripts\activate```
3. **Install dependencies:**
    pip install django django-crispy-forms crispy-bootstrap4 pillow
4. **Apply Migrations:**
    python manage.py makemigrations
    python manage.py migrate
5. **Create a Superuser (Admin):**
    python manage.py createsuperuser
6. **Run the Server:**
    python manage.py runserver


   Visit `http://127.0.0.1:8000/` to see the application.
---
## 🗄️ Database Integration
### Development (SQLite)
By default, this project uses **SQLite**, a file-based database that requires zero configuration. It's ideal for development because:
- The database is stored in a single file (`db.sqlite3`).
- No external server is required.
### Production (PostgreSQL)
For production environments, the project is structured to easily switch to **PostgreSQL**. This is handled by Django's database engine in `settings.py`.
### How it Works (Django ORM)
This project uses the **Django Object-Relational Mapper (ORM)**. Instead of writing raw SQL, we define our database tables as Python classes in `models.py`:
- **Models**: `Post`, `Category`, `User`, and `Profile`.
- **Relationships**:
  - `Post` to `User` (Many-to-One): Multiple posts can belong to one user.
  - `Post` to `Category` (Many-to-One): Multiple posts can have one category.
  - `User` to `Profile` (One-to-One): Each user has exactly one profile.
- **Migrations**: Every time you change a model, you run `makemigrations` to generate the SQL scripts and `migrate` to apply them to your database.
---
## ✨ Features So Far
- **User Authentication**: Sign-up, Login, Logout, and Password Reset.
- **Profiles**: Personalized profiles with profile pictures and automatic resizing via Pillow.
- **Blog Management**: Full CRUD (Create, Read, Update, Delete) functionality for posts.
- **Search & Filter**: Search posts by title and view posts by specific authors.
- **Pagination**: Browse through posts with easy navigation.
- **Categories**: Organize posts into different topics (newly added).
- **Styling**: Modern UI using Bootstrap 4 and Django Crispy Forms.