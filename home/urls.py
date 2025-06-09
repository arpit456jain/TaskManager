from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('', views.home, name='home'),
    path('task/', views.task, name='task'),
    path('todo/', views.todo, name='todo'),
    path('deletetask/<str:slug>', views.deletetask, name='deletetask'),
    path('edittask/<str:slug>', views.edittask, name='edittask'),
]
