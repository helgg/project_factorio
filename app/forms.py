from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'thumbnail']


# class SigninForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'repeat_password']




