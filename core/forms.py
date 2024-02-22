from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
