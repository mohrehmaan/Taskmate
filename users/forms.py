from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomRegisterForm(UserCreationForm):
    '''
    A form that creates a user, with no privileges, from the given username and
    password.
    '''
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField(initial="example@example.com")

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username',
                  'email', 'password1', 'password2']
