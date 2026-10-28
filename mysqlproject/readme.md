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


(work) C:\Users\user\django1\mysqlproject>python manage.py createsuperuser
Username (leave blank to use 'kaizentrix_design'): theju
Email address:
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.


