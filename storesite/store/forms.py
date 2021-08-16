from django import forms
from .models import Cart
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['product', 'username']