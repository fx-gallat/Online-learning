from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    intent = models.CharField(max_length=2000)
