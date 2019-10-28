from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Project(models.Model):
    project = models.ImageField(upload_to = 'projects/',null=True )
    title = models.CharField(max_length =30,null=True)
    project_description = models.CharField(max_length =30,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE ,null=True )
    project_link = models.URLField(max_length= 300,null=True)
    
    
    

    def __str__(self):
        return self.project_title

    def save_project(self):
        self.save()

    def delete_delete(self):
        self.delete()

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects


class Profile(models.Model):
    profile_photo= models.ImageField(upload_to = 'images/', null=True)
    bio = models.CharField(max_length =30)
    user = models.OneToOneField(User,on_delete=models.CASCADE ,related_name="profile",null=True)
    project = models.ForeignKey(Project,null=True)


    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    @classmethod
    def search_profile(cls, username):
        return cls.objects.filter(name__icontains=username)

    @classmethod
    def search_by_user(cls,search_term):
        profile = cls.objects.filter(title__icontains=search_term)
        return profile

    def save_profile(self):
        self.user
    def delete_profile(self):
        self.delete()


