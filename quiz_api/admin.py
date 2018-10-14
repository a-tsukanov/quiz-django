from django.contrib import admin

from .models import Quiz, Question, Answer


for model in (Quiz, Question, Answer):
    admin.site.register(model)
