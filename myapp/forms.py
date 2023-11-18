from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    # Customize the widgets for the fields
    username = forms.TextInput(attrs={'class': 'custom-widget-class'})
    first_name = forms.TextInput(attrs={'class': 'custom-widget-class'})
    last_name = forms.TextInput(attrs={'class': 'custom-widget-class'})
    email = forms.EmailInput(attrs={'class': 'custom-widget-class'})
    password1 = forms.PasswordInput(attrs={'class': 'custom-widget-class'})
    password2 = forms.PasswordInput(attrs={'class': 'custom-widget-class'})

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    # Customize the widgets for the fields
    username = forms.TextInput(attrs={'class': 'custom-widget-class'})
    first_name = forms.TextInput(attrs={'class': 'custom-widget-class'})
    last_name = forms.TextInput(attrs={'class': 'custom-widget-class'})
    email = forms.EmailInput(attrs={'class': 'custom-widget-class'})

class PasswordChangeCustomForm(PasswordChangeForm):
    # You can customize the PasswordChangeForm widgets here if needed
    pass
