python -m django startproject authauthproject

cd authauthproject
py manage.py startapp myapp


next the settings.py 
'myapp'


login.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Form</title>
</head>
<body>

    <center>
        <fieldset>
            <legend>Login Form</legend>

            <form method="POST">
                {% csrf_token %}

                <label>Username:</label>
                <input type="text" name="username"
                       placeholder="Enter username" required>

                <br><br>

                <label>Password:</label>
                <input type="password" name="password"
                       placeholder="Enter password" required>

                <br><br>

                <input type="submit" name="submit" value="Login">

            </form>
        </fieldset>
    </center>

</body>
</html>


next views.py
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.
def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponse("logged in successful")
        else:
            return render(request,'login.html',
                          {'error':'invalid username and password'})
    return render(request,'login.html')



next  url.py  

python manage.py makemigrations
python manage.py migrate

python manage.py showmigrations
python manage.py createsuperuser
