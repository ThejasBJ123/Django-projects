cd django1

.\work\scripts\activate


python -m django startproject modelproject

cd modelproject
D:\Thejas\Review_management_system\core\asgi.pycode .

python manage.py startapp myapp



python manage.py makemigrations myapp
python manage.py migrate


python manage.py check
python manage.py showmigrations

python manage.py createsuperuser




(work) C:\Users\user\django1\modelproject>python manage.py createsuperuser
Username (leave blank to use 'kaizentrix_design'): thejas
Email address: thejasbj66@gmail.com
Password:
Password (again):
Error: Your passwords didn't match.
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.




## Edited file 
----------

* model.py
* urls.py
* settings py
* template --- student html
* views.py 


