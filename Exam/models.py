from django.db import models
from Client.models import Client
from Questions.models import Question
from Category.models import Category


class SettingsExam(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    start_allow = models.DateTimeField()
    end_allow = models.DateTimeField()
    time = models.CharField(max_length=10, null=True, blank=True)
    attempts = models.IntegerField(default=1)
    Layout = models.IntegerField(default=5)
    Shuffle = models.BooleanField(default=True)
    preview = models.BooleanField(default=False)
    grade = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class Exam(models.Model):
    exam = models.ForeignKey(SettingsExam, on_delete=models.CASCADE)
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    sort_answer = models.CharField(max_length=100)
    answer = models.CharField(max_length=100, null=True, blank=True)
    score = models.BooleanField(default=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return str(self.id)
