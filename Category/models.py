from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    identity = models.CharField(max_length=10, unique=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)
