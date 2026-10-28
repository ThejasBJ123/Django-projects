from django.urls import path
from myapp.views import view1
urlpatterns = [
    path('my/',view1)
]
