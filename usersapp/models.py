from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an Username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Clients(AbstractBaseUser):

    class Types(models.TextChoices):
        # users type list
        DOCTOR = "DOCTOR", "Doctor"
        PATIENT = "PATIENT", "Patient"
        STAFF = "STAFF", "Staff"

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    type = models.CharField(
        _("Type"), max_length=100, choices=Types.choices, default=Types.DOCTOR)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class DoctorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Clients.Types.DOCTOR)


class PatientManger(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Clients.Types.PATIENT)


class StaffManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Clients.Types.STAFF)


class DoctorMore(models.Model):
    user = models.OneToOneField(Clients, on_delete=models.CASCADE)
    department = models.CharField(max_length=255)


class Doctor(Clients):
    objects = DoctorManager()

    @property
    def more(self):
        return self.doctormore

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Clients.Types.DOCTOR
        return super().save(*args, **kwargs)


class PatientMore(models.Model):
    user = models.OneToOneField(Clients, on_delete=models.CASCADE)
    disease = models.CharField(max_length=255)


class Patient(Clients):
    objects = PatientManger()

    @property
    def more(self):
        return self.patientmore

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Clients.Types.PATIENT
        return super().save(*args, **kwargs)


class StaffMore(models.Model):
    user = models.OneToOneField(Clients, on_delete=models.CASCADE)
    shift = models.CharField(max_length=40)


class Staff(Clients):
    objects = StaffManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Clients.Types.STAFF
        return super().save(*args, **kwargs)
