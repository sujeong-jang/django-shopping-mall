from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, username, password, phone):
        user = self.model(email=email, username=username, phone=phone)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username, password):
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(max_length=128, unique=True)
    password = models.CharField(max_length=500)
    username = models.CharField(max_length=20)
    phone = models.CharField(max_length=15, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return "<%d %s>" % (self.pk, self.email)