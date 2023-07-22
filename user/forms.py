from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(min_length=3,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "사용자 명을 입력하여 주시오."
                                },
                            ),
                            )
    password = forms.CharField(min_length=4,
                            widget=forms.PasswordInput(
                                attrs={
                                    "placeholder": "비밀번호를 입력하여 주시오."
                                },
                            ),
                            )


class SignupForm(forms.Form):
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
