from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class ProfileUserManager(BaseUserManager):
    """
    Manager model that allows register with no username
    """
    def _create_user(self, phone_number, password, **kwargs):
        if not phone_number:
            raise ValueError('Phone number must be set')
        user = self.model(phone_number=phone_number, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(phone_number, password, **kwargs)

    def create_superuser(self, phone_number, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self._create_user(phone_number, password, **kwargs)


class ProfileUser(AbstractUser):
    """
    Modified AbstractUser model with no username for use in this particular
    Bella project. Contains custom poles
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, unique=True)

    username = None
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = ProfileUserManager()

    def __str__(self):
        return self.phone_number
