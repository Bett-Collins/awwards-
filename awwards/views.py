from django.shortcuts import render
from django.http  import HttpResponse
from django.db import models
# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')

 Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=100,null=False)
    description=models.TextField(max_length=500)
    screenshot1=models.ImageField(default='default\.png',upload_to='screenshots/',blank=True)
    screenshot2=models.ImageField(default='default\.png',upload_to='screenshots/',blank=True)
    screenshot3=models.ImageField(default='default\.png',upload_to='screenshots/',blank=True)
    link=models.CharField(max_length=100,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)


    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

