import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class ProfileUserManager(BaseUserManager):
    """
    Manager model that allows register with no username
    """
    def _create_user(self, phone, password, **kwargs):
        """
        Creates user without password and username.
        Uses only phone number
        """
        if not phone:
            raise ValueError('Phone number must be set')
        user = self.model(phone=phone, **kwargs)
        user.set_password(password)
        user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(phone, password, **kwargs)

    def create_superuser(self, phone, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self._create_user(phone, password, **kwargs)


class ProfileUser(AbstractUser):
    """
    Modified AbstractUser model with no username for use in this particular
    Bella project. Contains custom poles
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, unique=True)
    activation_code = models.UUIDField(blank=True)

    username = None
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = ProfileUserManager()

    def create_activation_code(self):
        """
        Function that generates individual activation_code for each user
        for register/login
        """
        activation_code = uuid.uuid4()
        if ProfileUser.objects.filter(activation_code=activation_code).exist():
            self.create_activation_code()
        self.activation_code = activation_code
        self.save()
        return activation_code

    def __str__(self):
        return self.phone
