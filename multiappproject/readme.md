# Multi-App Project - Managing Multiple Apps in Django

A guide on creating and organizing multiple applications within a single Django project, with distinct views and endpoint routing.

---

## Project Structure Overview

```text
multiappproject/
│
├── multiappproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── firstapp/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── secapp/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── thirdapp/
│   ├── migrations/
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

### Step 1: Create Project and Multiple Applications

Open PowerShell in `C:\Users\user\django1`:

```powershell
PS C:\Users\user\django1> django-admin startproject multiappproject
PS C:\Users\user\django1> cd multiappproject
PS C:\Users\user\django1\multiappproject> python manage.py startapp firstapp
PS C:\Users\user\django1\multiappproject> python manage.py startapp secapp
PS C:\Users\user\django1\multiappproject> python manage.py startapp thirdapp
```

---

### Step 2: Register All Apps in `multiappproject/settings.py`

Add all three apps to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'firstapp',
    'secapp',
    'thirdapp',
]
```

---

### Step 3: Create Views for Each App

#### 1. In `firstapp/views.py`:
```python
from django.shortcuts import render
from django.http import HttpResponse

def home1(request):
    a = "<h1 style='color:red' > <u> Hello Everyone! Welcome to First App."
    return HttpResponse(a)
```

#### 2. In `secapp/views.py`:
```python
from django.shortcuts import render
from django.http import HttpResponse

def home2(request):
    return HttpResponse("Hello Everyone! Welcome to secound App.")
```

#### 3. In `thirdapp/views.py`:
```python
from django.shortcuts import render
from django.http import HttpResponse

def home3(request):
    return HttpResponse("Hello Everyone! Welcome to third App.")
```

---

### Step 4: Configure Project URLs in `multiappproject/urls.py`

Import views from all three apps and map them to separate endpoints:

```python
from django.contrib import admin
from django.urls import path
from firstapp.views import home1
from secapp.views import home2
from thirdapp.views import home3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', home1),
    path('second/', home2),
    path('third/', home3),
]
```

---

### Step 5: Run Server and Test

```powershell
PS C:\Users\user\django1\multiappproject> python manage.py runserver
```

Open your browser and test each route:
- `http://127.0.0.1:8000/first/` &rarr; Renders styled HTML header from `firstapp`.
- `http://127.0.0.1:8000/second/` &rarr; Renders response from `secapp`.
- `http://127.0.0.1:8000/third/` &rarr; Renders response from `thirdapp`.
