# Student Feedback Form - Django Project Documentation

A complete step-by-step guide to building the Django **Feedback Form** application with MySQL database integration and `ModelForm`.

---

## Project Structure Overview

```text
feedbackform/
│
├── feedbackform/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── myapp/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── template/
│   └── form.html
│
├── manage.py
└── readme.md
```

---

## Step-by-Step Implementation Guide

### Step 1: Create Django Project and App

Open PowerShell in your working directory `C:\Users\user\django1` and create the project:

```powershell
PS C:\Users\user\django1> django-admin startproject feedbackform
PS C:\Users\user\django1> cd feedbackform
PS C:\Users\user\django1\feedbackform> python manage.py startapp myapp
```

---

### Step 2: Configure `feedbackform/settings.py`

Modify `feedbackform/settings.py` to:
1. Register `myapp` under `INSTALLED_APPS`.
2. Configure the `template` folder path.
3. Configure MySQL database connection.

```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Define Template directory path
T = os.path.join(BASE_DIR, 'template')

# 2. Register 'myapp'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]

# 3. Configure Template DIRS
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [T],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 4. Configure MySQL Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stud',
        'USER': 'root',
        'PASSWORD': 'tEST@1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

> **Note:** Ensure you have the MySQL database driver installed:
> ```powershell
> PS C:\Users\user\django1\feedbackform> pip install mysqlclient
> ```
> *(Or `pip install pymysql` and add `pymysql.install_as_MySQLdb()` in `feedbackform/__init__.py` if needed)*

---

### Step 3: Define the Model in `myapp/models.py`

Create the `Student` model with fields for name, age, email, and feedback text:

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return self.name
```

---

### Step 4: Create the Form in `myapp/forms.py`

Initially, a standard `forms.Form` was drafted. Then, it was converted to a `forms.ModelForm` linked directly to the `Student` model.

In `myapp/forms.py`:

```python
# Initial standard Form (commented):
# class studnetform(forms.Form):
#     name = forms.CharField()
#     age = forms.IntegerField()
#     email = forms.EmailField(required=False)
#     feedback = forms.CharField()

from django import forms
from myapp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
```

---

### Step 5: Create Views in `myapp/views.py`

Handle both `GET` (render empty form) and `POST` (validate and save submitted form data to the database):

```python
from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import StudentForm

def form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Response Recorded")
    else:
        form = StudentForm()

    return render(request, 'form.html', {'form': form})
```

---

### Step 6: Create Template in `template/form.html`

Create a folder named `template` in the project root directory (`feedbackform/template/`), then create `form.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Student Form</title>
</head>
<body>

    <h1>Student Feedback Form</h1>

    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>

</body>
</html>
```

---

### Step 7: Configure Project URLs in `feedbackform/urls.py`

Route root endpoint `''` to `form_view`:

```python
from django.contrib import admin
from django.urls import path
from myapp.views import form_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', form_view),
]
```

---

### Step 8: Database Setup in MySQL

Open MySQL CLI or MySQL Workbench:

```sql
CREATE DATABASE stud;
SHOW DATABASES;
```

---

### Step 9: Make Migrations and Migrate

Run migrations from PowerShell to create the database tables:

```powershell
PS C:\Users\user\django1\feedbackform> python manage.py makemigrations
PS C:\Users\user\django1\feedbackform> python manage.py migrate
```

---

### Step 10: Run Server and Test

Start the Django development server:

```powershell
PS C:\Users\user\django1\feedbackform> python manage.py runserver
```

1. Open your browser and navigate to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
2. Fill out the feedback form (Name, Age, Email, Feedback) and click **Submit**.
3. You will receive the confirmation message: **"Response Recorded"**.
4. Verify the stored data in MySQL:
   ```sql
   USE stud;
   SELECT * FROM myapp_student;
   ```
