from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Введите email',
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите email'})
    )

    username = forms.CharField(
        label='Введите логин',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )

    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        label='Подтвердите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    check = forms.BooleanField(
        label="",
        required=True,
        help_text="Я согласен(на) с политикой конфиденциальности, пользовательским соглашением и даю согласие на обработку персональных данных."
    )

    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]


class UpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='Введите новый логин',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )

    email = forms.EmailField(
        label='Введите новый email',
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите email'})
    )

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileImageForm(forms.ModelForm):
    CHOICE = (('', '-----'), ('male', 'Мужской'), ('female', 'Женский'))

    img = forms.ImageField(
        label='Выберите новое фото',
        required=False,
        widget=forms.FileInput
    )

    gender = forms.CharField(
        label='Выберите пол',
        required=False,
        widget=forms.Select(
            choices=CHOICE,
            attrs={'class': 'form-control', }
        )
    )

    check = forms.BooleanField(
        label="",
        required=False,
        help_text="Согласие на рассылку"
    )

    class Meta:
        model = Profile
        fields = ['img', 'gender', 'check']
