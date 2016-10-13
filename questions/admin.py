from django.contrib import admin
from .models import Subject, Question, Answer

class SubjectAdmin(admin.ModelAdmin):
    class Meta:
        model = Subject


class QuestionAdmin(admin.ModelAdmin):
    class Meta:
        model = Question

class AnswerAdmin(admin.ModelAdmin):
    class Meta:
        model = Answer

admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Answer)