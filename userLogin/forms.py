from django import forms
from django.contrib.auth.models import User
from .models import Profile

class user_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class profile_form(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ('avatar','steam')
