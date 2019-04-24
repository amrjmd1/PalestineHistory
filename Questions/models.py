from django.db import models
from PalestineHistory.settings import *
from Category.models import Category


class Question(models.Model):
    question = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    answer_1 = models.CharField(max_length=100)
    answer_2 = models.CharField(max_length=100)
    answer_3 = models.CharField(max_length=100)
    answer_4 = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)


class ExcelFiles(models.Model):
    title = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to='excel_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

