# First Project - Introduction to Django Views & URLs

A foundational guide on creating your first Django project, setting up an application, writing HTTP views, and configuring project-level URL routing.

---

## Project Structure Overview

```text
firstproject/
│
├── firstproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── myapp/
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── manage.py
└── readme.md
```

---

## Step-by-Step Implementation Guide

### Step 1: Create Django Project and App

Open PowerShell in `C:\Users\user\django1` and run:

```powershell
PS C:\Users\user\django1> django-admin startproject firstproject
PS C:\Users\user\django1> cd firstproject
PS C:\Users\user\django1\firstproject> python manage.py startapp myapp
```

---

### Step 2: Register App in `firstproject/settings.py`

Open `firstproject/settings.py` and add `'myapp'` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]
```

---

### Step 3: Create Views in `myapp/views.py`

Define view functions that return simple HTTP responses:

```python
from django.shortcuts import render
from django.http import HttpResponse

def views1(request):
    a = "Welcome to Django session"
    return HttpResponse(a)

def views2(request):
    b = "hello Everone "
    return HttpResponse(b)
```

---

### Step 4: Configure URLs in `firstproject/urls.py`

Import the views and map them to endpoint URLs:

```python
from django.contrib import admin
from django.urls import path
from myapp.views import views1, views2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('res1/', views1),
    path('res2/', views2),
]
```

---

### Step 5: Run the Server and Test

Start the Django development server:

```powershell
PS C:\Users\user\django1\firstproject> python manage.py runserver
```

Open your browser and navigate to:
- `http://127.0.0.1:8000/res1/` &rarr; Displays: `"Welcome to Django session"`
- `http://127.0.0.1:8000/res2/` &rarr; Displays: `"hello Everone "`
