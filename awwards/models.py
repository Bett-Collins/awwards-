from django.db import models


# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=100,null=False)
    link=models.CharField(max_length=100,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)


    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()
class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    bio = TextField(max_length=500,null=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,blank=True)
    name =models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
class Myprojects(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
class Myprofile(models.Model):
    name = models.CharField(max_length=40)
    bio = models.TextField()
    email = models.EmailField()
    
