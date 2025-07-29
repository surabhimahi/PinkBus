from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
    class Meta:
        model = User
        fields =('username', 'email', 'password1', 'password2')
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)