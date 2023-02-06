from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDesc = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)