from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm): # 내장 회원가입 폼을 상속받아서 확장한다.
    email = forms.EmailField(required=True) # 이메일 필드 추가

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")