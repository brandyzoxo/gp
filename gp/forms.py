import email

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from gp.models import Commerce


class CommerceForm(forms.ModelForm):
    class Meta:
        model = Commerce
        fields= ['name','email','subject','message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}),
           ' subject': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Message'}),
        }
