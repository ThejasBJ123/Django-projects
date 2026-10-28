.\work\scripts\activate


django-admin startproject productproject1

cd productproject

python manage.py startapp myapp

next model.py


python manage.py makemigrations



python manage.py makemigrations myapp
python manage.py migrate


python manage.py check
python manage.py showmigrations

python manage.py createsuperuser


(work) C:\Users\user\django1\productproject>python manage.py createsuperuser
Username (leave blank to use 'kaizentrix_design'): theju
Email address:
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

python manage.py runserver


http://127.0.0.1:8000/admin/



