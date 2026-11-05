# Arithmetic Operation Project - Django Views

A guide on performing arithmetic operations in a Django view and returning the calculated result as an HTTP response.

---

## Project Structure Overview

```text
arithopproject/
│
├── arithopproject/
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
PS C:\Users\user\django1> django-admin startproject arithopproject
PS C:\Users\user\django1> cd arithopproject
PS C:\Users\user\django1\arithopproject> python manage.py startapp myapp
```

---

### Step 2: Register App in `arithopproject/settings.py`

Add `'myapp'` to `INSTALLED_APPS`:

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

### Step 3: Create View in `myapp/views.py`

Define the `add` view function to calculate sum:

```python
from django.shortcuts import render
from django.shortcuts import HttpResponse

def add(request):
    a = int(input("Enter a n1: "))
    b = int(input("Enter a n2: "))
    c = a + b
    return HttpResponse(str(c))
```

---

### Step 4: Configure URLs in `arithopproject/urls.py`

Map the endpoint path `'add1/'` to the `add` view:

```python
from django.contrib import admin
from django.urls import path
from myapp.views import add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add1/', add),
]
```

---

### Step 5: Run Server and Test

Start the development server:

```powershell
PS C:\Users\user\django1\arithopproject> python manage.py runserver
```

1. Open your browser and navigate to: `http://127.0.0.1:8000/add1/`
2. Check your PowerShell terminal prompt to enter numbers when requested.
3. The result of the addition will be rendered in the browser.
