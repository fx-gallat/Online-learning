from __future__ import unicode_literals
from django.db import models
from django.urls import reverse


class Question(models.Model):
    question_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    intent = models.CharField(max_length=2000)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Question.
        """
        return reverse('question-detail-view', args=[str(self.id)])

    def __str__(self):

        return self.question_text