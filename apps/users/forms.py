from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)


class LoginForm(AuthenticationForm):
    captcha = ReCaptchaField()

    def clean(self):
        captcha = self.cleaned_data.get("captcha")
        if not captcha:
            return
        return super().clean()


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)
