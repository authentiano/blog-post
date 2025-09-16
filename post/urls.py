
from django.contrib import admin
from django.urls import path
from post import views as views
urlpatterns = [
    path('',views.home, name= "home"),
    path('blog',views.blog, name= "blogpost")
]
