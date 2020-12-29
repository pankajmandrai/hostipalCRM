from enum import IntEnum

from django.contrib.auth.models import AbstractUser
from django.db import models


class RoleList(IntEnum):
    Admin = 1
    Doctor = 2
    Patient = 3
    LabStaff = 4

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class User(AbstractUser):
    role = models.PositiveSmallIntegerField(choices=RoleList.choices(), default=RoleList.Patient)
    address1 = models.CharField("Address 1", max_length=200, blank=True)
    address2 = models.CharField("Address 2", max_length=200, blank=True)
    city = models.CharField("City", max_length=50, blank=True)
    state = models.CharField("State", max_length=50, blank=True)
    country = models.CharField("State", max_length=50, blank=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True)

