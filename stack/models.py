import email
from tabnanny import verbose
from django.db import models

# Create your models here.

class UserName(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.username
        

class Message(models.Model):
    message = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UserName', on_delete=models.CASCADE,related_name='messages')
