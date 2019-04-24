from django.db import models
from Category.models import Category


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    identity = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)
