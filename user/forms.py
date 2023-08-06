from django import forms
from django.core.exceptions import ValidationError

from .models import User


class LoginForm(forms.Form):

    username = forms.CharField(min_length=3,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "사용자 명을 입력하여 주시오.",
                                    "classname": "input__form",
                                },
                            ),
                            )
    password = forms.CharField(min_length=4,
                            widget=forms.PasswordInput(
                                attrs={
                                    "placeholder": "비밀번호를 입력하여 주시오.",
                                    "classname": "input__form",
                                },
                            ),
                            )


class SignupForm(forms.Form):

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError(f'입력한 사용자명{username}은 사용중 입니다.')
        return username

    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password2 != password1:
            self.add_error("password2", "비밀번호와 비밀번호 확인란의 입력값이 다릅니다.")

    def save(self):
        username = self.cleaned_data["username"]
        password1 = self.cleaned_data["password1"]
        user = User.objects.create_user(
            username=username,
            password=password1,
        )
        return user
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "사용하실 닉네임을 입력하시오"
        },
    ), )
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "사용할 비밀번호를 입력하여 주십시오"
        },
    ),
    )
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "사용할 비밀번호를 입력하여 주십시오"
        },
    ),
    )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
        ]
        password = forms.CharField(min_length=4,
                                   widget=forms.PasswordInput(
                                       attrs={
                                           "placeholder": "비밀번호를 입력하여 주시오.",
                                       },
                                   ),
                                   )