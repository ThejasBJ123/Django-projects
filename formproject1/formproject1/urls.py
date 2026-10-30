from django.contrib import admin
from django.urls import path
from myapp.views import Student_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Student_list),
]