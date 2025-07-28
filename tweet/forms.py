from django import forms
from .models import Tweet, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets ={
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'What\'s happening?'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets ={
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'}),
        }
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')