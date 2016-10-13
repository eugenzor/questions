from django.forms import ModelForm, Textarea
from .models import QuestionVersioned, Answer


class QuestionForm(ModelForm):
    class Meta:
        model = QuestionVersioned
        fields = ['text']
        widgets = {
            'text': Textarea(attrs={'rows': 3}),
        }

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text']
        labels = {'text': ''}
