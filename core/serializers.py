from rest_framework import serializers
from .models import Hint, Quiz, Answer, Question


class HintSerializer(serializers.HyperlinkedModelSerializer):
    publish_date = serializers.DateTimeField(format='%d-%B-%Y %H:%M')

    class Meta:
        model = Hint
        fields = ('url', 'id', 'title', 'content', 'tags', 'publish_date')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
