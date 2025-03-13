import email

from django import forms

from gp.models import Commerce


class CommerceForm(forms.ModelForm):
    class Meta:
        model = Commerce
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}),
           ' subject': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Message'}),
        }