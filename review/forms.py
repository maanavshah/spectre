from django import forms
from .models import Post, User, Hit, Comment
from django.contrib.auth import authenticate

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    def login(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class HitForm(forms.ModelForm):
    class Meta:
        model = Hit
        fields = ('tag', 'hit_count')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)