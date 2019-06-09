from django.db import models
from tagging.fields import TagField

# Create your models here.


class Hint(models.Model):
    title = models.CharField(max_length=255, verbose_name='Tytuł')
    content = models.TextField(verbose_name='Zawartosć')
    tags = TagField(verbose_name='Tagi')
    publish_date = models.DateTimeField(verbose_name='Data publikacji')

    class Meta:
        ordering = ('publish_date', )

    def __str__(self):
        return self.title


class Question(models.Model):
    hint = models.ForeignKey(Hint, on_delete=models.CASCADE, verbose_name='Porada')
    question = models.TextField()
    positive_answer = models.TextField()
    negative_answer1 = models.TextField()
    negative_answer2 = models.TextField()

    def __str__(self):
        return self.question


class Quiz(models.Model):
    hint = models.ForeignKey(Hint, on_delete=models.CASCADE, related_name='quiz')
    question = models.ManyToManyField(Question, related_name='quiz')

    def __str__(self):
        return self.hint.title
