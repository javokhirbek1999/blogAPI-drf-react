from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, username, name, password=None, **kwargs):

        if not email:
            raise ValueError(_('Email is required'))
        
        email = self.normalize_email(email)

        user = self.model(email=email, name=name)

        user.set_password(password)

        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, username, name, password):

        user = self.create_user(email, username, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=250, unique=True)
    username = models.CharField(max_length=250, unique=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','name']

    objects = UserManager()

    def __str__(self):
        return self.email
    