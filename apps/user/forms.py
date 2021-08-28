from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    email = forms.EmailField() # default Req=True
    
    class Meta:
        '''
        model = what model is this for, when ever this form validates its gonna create BUser
        and when we say form.save() its gonna be saved to this User model
        the fields that are going to be shown on form, and order
        '''
        model = User
        fields = ['username', 'email', 'password1', 'password2']

