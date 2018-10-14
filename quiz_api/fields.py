from rest_framework import serializers
from .models import Quiz, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('answer', 'is_correct')


class QuestionSerializer(serializers.ModelSerializer):
    answer_set = AnswerSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Question
        fields = ('question', 'answer_set')


class QuizSerializer(serializers.ModelSerializer):
    question_set = QuestionSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Quiz
        fields = ('name', 'question_set')
