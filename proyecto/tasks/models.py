from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class tasks(models.Model):
    title= models.CharField(max_length=100)
    description=models.CharField(max_length=100, blank=True)
    created= models.DateTimeField(auto_now_add=True)
    datecompleted=models.DateTimeField(null=True)
    important=models.BooleanField(default= False)
    User=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) :
        return self. title + '- by' + self.User.username

