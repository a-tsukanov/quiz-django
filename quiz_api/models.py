from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.CharField(max_length=100)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.quiz}] {self.question}'


class Answer(models.Model):
    answer = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'[{self.question.quiz}] {self.question.question[:70]}: {self.answer}'

