from enum import IntEnum
from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager
# from .admin import UserManager
from django.db import models

class RoleList(IntEnum):
    Admin = 1
    Doctor = 2
    Patient = 3
    LabStaff = 4

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_admin=False, is_staff=False,
                    is_active=True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)  # change password to hash
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.admin = True
        user.staff = True
        user.active = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user_group",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="user_permissions",
    )

    email = models.EmailField('email address', unique=True)  # changes email to unique and blank to false
    #role = models.PositiveSmallIntegerField(choices=RoleList.choices(), default=RoleList.Patient)
    address1 = models.CharField("Address 1", max_length=200, blank=True)
    address2 = models.CharField("Address 2", max_length=200, blank=True)
    city = models.CharField("City", max_length=50, blank=True)
    state = models.CharField("State", max_length=50, blank=True)
    country = models.CharField("State", max_length=50, blank=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True)

    REQUIRED_FIELDS = []
    #objects = UserManager()
