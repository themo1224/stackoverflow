from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your email'}))
    password1 = forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'your pass'}))
    password2 = forms.CharField(label="confirm password",widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'your pass'}))
    
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
#  first email is one of the user field and the right one is the var #
        if user:
            raise ValidationError('this email is already in use')
        return email
        
    def clean_username(self):
        username= self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('this username is already in use')
        return username
            
#  Clean def is used when we want to validate tow parameters that are related to each other  #
            
    def clean(self):
        cd= super().clean()
        p1= cd.get('password1')
        p2= cd.get('password2')
        
        if p1 and p2 and p1 != p2:
            raise ValidationError('passwords most match')
        
        
class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'your pass'}))
    
            