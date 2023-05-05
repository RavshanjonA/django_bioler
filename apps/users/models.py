from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import BooleanField, CharField, EmailField, ImageField, ManyToManyField
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel
from apps.users.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    username = CharField(verbose_name=_("Username"), max_length=128, unique=True)
    phone_number = PhoneNumberField(verbose_name=_("Phone number"), region="UZ", unique=True)
    email = EmailField(verbose_name=_("Email address"), unique=True)

    first_name = CharField(verbose_name=_("First name"), max_length=124)
    last_name = CharField(verbose_name=_("Last name"), max_length=124)
    profile_photo = ImageField(
        verbose_name=_("Profile photo"), upload_to="images/accounts/profile/%Y/%m/%d/", blank=True, null=True
    )
    is_staff = BooleanField(verbose_name=_("Is staff?"), default=False)
    is_active = BooleanField(verbose_name=_("Is active?"), default=True)
    is_superuser = BooleanField(verbose_name=_("Is superuser?"), default=False)

    groups = ManyToManyField(verbose_name=_("Groups"), to="auth.Group", related_name="users", blank=True)

    objects = CustomUserManager()  # noqa F821

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email
