from django import forms
from .models import TodoMdel
from django.contrib.auth.models import User

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoMdel
        fields = "__all__"

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name']