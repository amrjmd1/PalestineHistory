from django.db import models
from Category.models import Category


# Create your models here.
class Manager(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + " || " + str(self.username)


class Client(models.Model):
    email = models.CharField(max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    grand_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    gender = models.CharField(max_length=4)
    is_active = models.BooleanField(default=False)
    identity = models.CharField(max_length=15)

    def __str__(self):
        return str(self.id)


class UserAgents(models.Model):
    ip = models.CharField(max_length=25, null=True, blank=True)
    user = models.CharField(max_length=60)
    browser_family = models.CharField(max_length=30, null=True, blank=True)
    browser_version = models.CharField(max_length=15, null=True, blank=True)
    os_family = models.CharField(max_length=30, null=True, blank=True)
    os_version = models.CharField(max_length=15, null=True, blank=True)
    device_family = models.CharField(max_length=30, null=True, blank=True)
    start_session = models.DateTimeField(auto_now=False, auto_now_add=True)
    end_session = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    logout = models.BooleanField(default=False)
    manage = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + " || " + str(self.user)


class LoginAttempts(models.Model):
    ip = models.CharField(max_length=25, null=True, blank=True)
    name = models.CharField(max_length=40, null=True, blank=True)
    password = models.CharField(max_length=40, null=True, blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    browser_family = models.CharField(max_length=30, null=True, blank=True)
    browser_version = models.CharField(max_length=15, null=True, blank=True)
    os_family = models.CharField(max_length=30, null=True, blank=True)
    os_version = models.CharField(max_length=15, null=True, blank=True)
    device_family = models.CharField(max_length=30, null=True, blank=True)
    manage = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + " || " + str(self.name)


class VerifyEmail(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    random_number = models.CharField(max_length=10, null=True, blank=True)
