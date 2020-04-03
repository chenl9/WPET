from django.urls import path, include, re_path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.homepage, name="home"),
]
