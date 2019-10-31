from django.test import TestCase
from .models import Project,Profile,Review

# Create your tests here.
class ProjectTestClass(TestCase):

    def setUp(self):
        # Creating a new image and saving it
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