from django.urls import path, include, re_path
from . import views


app_name = 'website'

urlpatterns = [
    path('home/', views.homepage, name="home"),
    path('WPET/', views.WPET, name="WPET"),
    path('Q&A/', views.QandA, name="QandA"),
    path('team/', views.teaminfo, name="team"),
    path('milestone/', views.milestone, name="milestone"),
    path('prototype/', views.prototype, name="prototype"),
    path('testing/', views.testing, name="testing"),
]
