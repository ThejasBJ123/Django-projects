.\work\scripts\activate

django-admin startproject mysqlproject
cd mysqlproject

python manage.py startapp myapp



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'student',
        'USER':'root',
        'PASSWORD':'tEST@1234',
        'HOST':'localhost',
        'post':'3306',
    }
}



pip install mysqlclient


python manage.py makemigrations myapp
python manage.py migrate


problem

-------
(work) C:\Users\user\django1 --->

python  -m django --version
python -m pip install "Django>=5.2,<5.3"


