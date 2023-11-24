from.import views
from django.urls import path

urlpatterns=[
    path('',views.demo,name='demo'),
    path('login',views.login,name='login'),
    path('newpage',views.newpage,name='newpage'),
    path('form',views.form,name='form'),
    path('register/',views.register,name='register'),
    path('home',views.home,name='home')
]