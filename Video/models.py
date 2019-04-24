from django.db import models


# Create your models here.
class Video(models.Model):
    title = models.TextField()
    description = models.TextField(null=True, blank=True)
    poster = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
