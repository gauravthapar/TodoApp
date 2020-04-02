from django.forms import ModelForm 
from .models import Todo
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important','duedate']


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Already exist")
        return email