from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    task=models.TextField(max_length=1000)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class user_data(models.Model):
    first=models.CharField(max_length=40)
    last=models.CharField(max_length=40)
    email=models.EmailField(max_length=40,unique=True,editable=False)
    phone=models.IntegerField(unique=True,editable=False)
    
