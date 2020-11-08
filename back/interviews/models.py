from django.db import models
from django.conf import settings

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)

    class Meta:
        app_label = 'interviews'


class Question(models.Model):
    class Meta:
        app_label = 'interviews'
    question = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    time = models.IntegerField()


class Interview(models.Model):
    class Meta:
        app_label = 'interviews'
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default="GUEST")
    used_questions = models.ManyToManyField(
        Question, related_name='used_interviews')
