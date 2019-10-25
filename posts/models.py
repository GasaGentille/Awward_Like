from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Project(models.Model):
    project = models.ImageField(upload_to = 'projects/',null=True )
    project_name = models.CharField(max_length =30)
    project_caption = models.CharField(max_length =30)
    user = models.ForeignKey(User,on_delete=models.CASCADE ,null=True )
    
    
    

    def __str__(self):
        return self.project_name

    def save_project(self):
        self.save()

    def delete_delete(self):
        self.delete()


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


