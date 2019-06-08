from django.db import models
from tagging.fields import *

# Create your models here.


class Hint(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = TagField()
    publish_date = models.DateTimeField()

    class Meta:
        ordering = ('publish_date', )


class Quiz(models.Model):
    hint = models.OneToOneField(Hint, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()  # in form must be RadioSelectField
