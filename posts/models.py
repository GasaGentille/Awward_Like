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
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    

    def __str__(self):
        return self.title

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

    def save_profile(self):
        self.user
    def delete_profile(self):
        self.delete()

class Rate(models.Model):
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)