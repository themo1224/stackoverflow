from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'your email'}))
    password = forms.CharField(label="password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'your pass'}))
