from .models import Project,Profile,Review
from django import forms

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project','title','project_description','project_link')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio')
        exclude=['user']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio')
        exclude=['user']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['design', 'content','usability','rating']
        
