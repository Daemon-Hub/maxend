from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-lg'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-lg'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control form-control-lg'
            })
        }

    def clean_username(self):
        import re
        username = self.cleaned_data['username']
        reg = r"\A[\w\d\s]+[\w\d\s\-_]*"
        if not re.fullmatch(reg, username):
            raise ValidationError(
                "Имя пользователя может состоять только из букв, цифр и знаков: -_ ."
            )
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if not len(password) >= 8:
            raise ValidationError(
                "Пароль должен составлять как минимум 8 символов."
            )
        return password
