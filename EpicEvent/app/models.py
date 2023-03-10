from datetime import datetime
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'management')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    ROLE_CHOICES = (
        ('sales', 'sales'),
        ('management', 'management'),
        ('support', 'support')
    )

    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


class Client(models.Model):
    STATUS_CHOICES = (
        ('potential', 'potential'),
        ('existing', 'existing'),
    )

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    sales_contact = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='clients')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.email


class Contract(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()
    amount = models.FloatField()
    payment_due = models.DateTimeField(auto_now_add=False)
    sales_contact = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='sales_contracts')
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, related_name='client_contracts')

    def __str__(self):
        return str(self.pk)


class Event(models.Model):
    STATUS_CHOICES = (
        ('created', 'created'),
        ('in_progress', 'in_progress'),
        ('finished', 'finished')
    )

    name = models.CharField(max_length=30, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    attendees = models.IntegerField()
    event_date = models.DateTimeField(auto_now_add=False)
    notes = models.TextField(null=True, blank=True)
    support_contact = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='support_events')
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, related_name='client_events')
    contract = models.OneToOneField(to=Contract, on_delete=models.CASCADE, related_name='contract_event')


def update_date(sender, instance, **kwargs):
    instance.date_updated = datetime.now()


models.signals.pre_save.connect(update_date, sender=Client)
models.signals.pre_save.connect(update_date, sender=Contract)
models.signals.pre_save.connect(update_date, sender=Event)

