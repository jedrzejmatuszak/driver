from rest_framework import serializers
from .models import Hint, Quiz, Question


class HintSerializer(serializers.HyperlinkedModelSerializer):
    publish_date = serializers.DateTimeField(format='%d-%B-%Y %H:%M')
    hint_detail = serializers.HyperlinkedIdentityField(view_name='hint-detail', read_only=True)

    class Meta:
        model = Hint
        fields = ('hint_detail', 'id', 'title', 'content', 'tags', 'publish_date', 'quiz')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    hint = serializers.HyperlinkedRelatedField(view_name='hint-detail', read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'question', 'positive_answer', 'negative_answer1', 'negative_answer2', 'hint')


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    question = serializers.HyperlinkedRelatedField(many=True, view_name='question-detail', read_only=True)
    title = serializers.ChoiceField(choices=[x.title for x in Hint.objects.all()])

    class Meta:
        model = Quiz
        fields = ('id', 'title', 'question')
