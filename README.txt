# Student Management System

Student mangagement sysem is a web application with functionalities such as display student list and student detail, add and edit student, and user authentication. This project is built with Django web framework.

## Installation

Use the following git command to download the project.

```bash
git clone https://github.com/Xinye130/Xinye_GNG5300_Student_Management.git
```

## Setup and Run

Please run all the following commands in git bash.

First cd into directory Xinye_GNG5300_Student_Management, then run the following command to activate the virtual environment.

```bash
source venv/Scripts/activate
```

Start the server:
```bash
(venv) $ python manage.py runserver
```

Then go to http://localhost:8000 in the browser to check the application.

## Testing Admin

To test admin functionalities in http://localhost:8000/admin, you may use the superuser account:
```python
Username: Xinye130
Password: adminadmin
```

To enable Django default CSS style for admin, in student_management/settings, please set:
```python
DEBUG = True
```
Also please don't forget to change it back to False to check customized 404 page.