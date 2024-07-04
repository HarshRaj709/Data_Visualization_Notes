from django.urls import path
from . import views

urlpatterns = [
    path('',views.username,name='username'),
    path('home/<str:username>/', views.home, name='home'),
]
