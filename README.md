# Project Management System

## Description
A Django-based project management system with the ability to manage users, projects, tasks, comments, and project members. The system provides the following functionality:

- User registration, login, and management.
- Project creation, modification, and deletion.
- Task management within projects, including status, priority, and due dates.
- Commenting on tasks for collaboration.

## Requirements

### Prerequisites
- Python 3.x
- Django 5.1.3 (or compatible version)
- MySQL (or another relational database of your choice)
- Django REST Framework
- Postman (for API testing)

### Setup Instructions

#### 1. Clone the Repository
Clone the repository to your local machine using the following command: git clone https://github.com/username/project-management-system.git
### 2. Create a Virtual Environment
cd project-management-system
python -m venv venv
Activate the virtual environment:  venv\Scripts\activate
### 3.  Install Dependencies
Install the required packages by running: pip install -r requirements.txt

### 4. Configure Database
The default configuration uses MySQL, but you can modify the DATABASES setting in the settings.py file to use a different database system.

For MySQL, ensure that your MySQL server is running, and create a database named project_management

CREATE DATABASE project_management;
Then, update your settings.py with the correct database credentials:

### DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'project_management',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
### 5. Run Migrations
  Once your database is set up, run migrations to create the database schema:
           python manage.py migrate

   
### 6. Create a Superuser
        To access the Django admin panel, you need to create a superuser account:
              python manage.py createsuperuser
  
Follow the prompts to enter the username, email, and password for the superuser.

### 7. Run the Development Server
  Start the Django development server:
  
          python manage.py runserver

      
Your API should now be available at http://localhost:8000/.
