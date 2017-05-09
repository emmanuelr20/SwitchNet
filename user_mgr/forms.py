from django import forms
from django.contrib.auth.models import User
from .models import UserAccount, FriendList, Address

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length = 120, help_text = '150 characters or fewer. Letters, digits and @/./+/-/_ only.', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Username', 'required': 'required'}))
    first_name = forms.CharField(max_length = 120, help_text = '', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'First Name', 'required': 'required'}))
    last_name = forms.CharField(max_length = 120, help_text = '',  widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Surname', 'required': 'required'}))
    email = forms.EmailField(max_length = 120,  help_text = '',  widget = forms.EmailInput(attrs = {'class': 'form-control', 'placeholder': 'email@example.com', 'required': 'required'}))
    password = forms.CharField(max_length = 15, help_text = '',  widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'password', 'required': 'required'}))

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password',)

class LoginForm(forms.ModelForm):
    email = forms.EmailField(max_length = 120,  help_text = '',  widget = forms.EmailInput(attrs = {'class': 'form-control', 'placeholder': 'email@example.com', 'required': 'required'}))
    password = forms.CharField(max_length = 15, help_text = '',  widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'password', 'required': 'required'}))
    
    class Meta:
        model = User
        fields = ('email', 'password',)

class UserAccountForm(forms.ModelForm):
    phone_number = forms.CharField(max_length = 120, help_text = '', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'First Name', 'required': 'required'}))
    
    class Meta:
        model = UserAccount
        fields = ('phone_number', 'gender', 'status')
