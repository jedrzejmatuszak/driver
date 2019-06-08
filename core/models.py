from django.db import models
from tagging.fields import TagField

# Create your models here.


class Hint(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = TagField()
    publish_date = models.DateTimeField()

    class Meta:
        ordering = ('publish_date', )


class Answer(models.Model):
    positive_answer = models.TextField()
    negative_answer1 = models.TextField()
    negative_answer2 = models.TextField()


class Quiz(models.Model):
    hint = models.OneToOneField(Hint, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)  # in form must be RadioSelectField
