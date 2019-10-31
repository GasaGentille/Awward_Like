from django.test import TestCase
from .models import Project,Profile,Review

# Create your tests here.
class ProjectTestClass(TestCase):

    def setUp(self):
        # Creating a new project and saving it
        self.new_project= Project(project ='projects/', title ='galery', project_description = "Django galery")

    # Testing  instance

    def test_instance(self):
        self.assertTrue(isinstance(self.new_project,Project))

   # Testing Save Method
    def test_save_project(self):
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0) 

    #test delete
    def test_delete_project(self):
        self.new_project.save_project()
        project = Project.objects.filter(title='galery').first()
        delete = Project.objects.filter(title = project.title).delete()
        projects = Project.objects.all()
        self.assertFalse(len(projects)==1)

class ProfileTestClass(TestCase):

    def setUp(self):
        # Creating a new profile and saving it
        self.new_profile= Profile(profile_photo ='images/', bio ='pray')

    # Testing  instance

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

   # Testing Save Method
    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertFalse(len(profiles) > 0) 

    #test delete
    def test_delete_profile(self):
        self.new_profile.save_profile()
        profile = Profile.objects.filter(bio='pray').first()
        delete = Profile.objects.filter().delete()
        profiles = Profile.objects.all()
        self.assertFalse(len(profiles)==1)