from django.urls import path, re_path
from .views import login


urlpatterns = [
    path('login', login)
]
