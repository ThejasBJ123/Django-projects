
from django.contrib import admin
from django.urls import path

from myapp.views import user_login, user_register, dashboard, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('dash/', dashboard, name='dashboard'),
    path('logout/', user_logout, name='logout'),
]
