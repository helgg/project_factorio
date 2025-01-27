from django import forms
from .models import Blog, Profile

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'thumbnail']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio_details', 'profile_photo']




