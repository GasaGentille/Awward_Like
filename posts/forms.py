from .models import Project,Profile
from django import forms

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project','project_caption','user')

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

