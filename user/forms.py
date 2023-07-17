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


