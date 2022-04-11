from django.contrib.auth.models import User
from django.test import TestCase
from .models import Profile,Project

# Create your tests here.
#setup method
class ProjectTestclass(TestCase):
   
    def setUp(self):
        self.projects=Project(title='mytitle',description='description',screenshot1='s1',screenshot2='s2',screenshot3='s3',link='link')

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.projects,Project))
    #save method
    def test_save_project(self):
        self.projects.save_project()
        projects=Project.objects.all()
        self.assertTrue(len(projects)>0) 

        #delete method
    def test_delete_project(self):
        self.projects.save_project()
        project_record=Project.objects.all()
        self.projects.delete_project()
        self.assertTrue(len(project_record)==0)



class ProfileTestclass(TestCase):
    #setup method
    def setUp(self):
        self.myprofile=Profile(profile_pic='image',bio='Hardworking',email='email@gmail.com',avatar='avatar')

     #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.myprofile,Profile))

    #save method
    def test_save_profile(self):
        self.myprofile.save_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>0)

    def test_delete_profile(self):
        self.myprofile.save_profile()
        profile_record=Profile.objects.all()
        self.myprofile.delete_profile()
        self.assertTrue(len(profile_record)==0)