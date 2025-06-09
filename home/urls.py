from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('', views.home, name='home'),
    path('task/', views.task, name='task'),
    path('deletetask/<str:id>', views.deletetask, name='deletetask'),
    path('edittask/<str:id>', views.edittask, name='edittask'),
]
