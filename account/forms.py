from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control' , 'placeholder': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))