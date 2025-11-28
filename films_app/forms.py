from django import forms
from .models import Film, FilmScore, FilmComment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title','description', 'genre', 'photoname']


        
class FilmScoreForm(forms.ModelForm):
    class Meta:
        model = FilmScore
        fields = ['score']


class FilmCommentForm(forms.ModelForm):
    class Meta:
        model = FilmComment
        fields = ['comment']

class FilmUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
