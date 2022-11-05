from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, name=None, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.staff = is_staff
        user.name = name
        user.username = username
        user.admin = is_admin
        # user.active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, password=None):
        user = self.create_user(email, password=password, name=name, username=username)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_("ФИО"), max_length=70)
    username = models.CharField(_("Имя пользователя"), max_length=150, unique=True)
    email = models.EmailField(_("Почта"), unique=True)
    birthday_date = models.DateField(_("Год рождения"), auto_now=True)
    genders = models.ForeignKey("users.Genders", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(_("Время создания"), auto_now=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "username"]

    objects = UserManager()

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def __str__(self):
        return self.email


class Genders(models.Model):
    title = models.CharField(_("Пол"), max_length=20)
