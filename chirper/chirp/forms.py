from django import forms
from .models import chirp
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class chirpform(forms.ModelForm):
    class Meta:
        model = chirp
        fields = ['text','photo']

class registrationform(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')