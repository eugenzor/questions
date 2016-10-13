from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.urls import reverse, reverse_lazy
from .models import Question, QuestionVersioned, Answer
from .forms import QuestionForm, AnswerForm


class QuestionListView(ListView):
    def get_queryset(self):
        query_set = Question.objects.filter(actual=True)
        return query_set


class QuestionVersionsView(ListView):
    model = QuestionVersioned


class QuestionCreateView(SuccessMessageMixin, CreateView):
    model = QuestionVersioned
    form_class = QuestionForm
    template_name = 'questions/question_create.html'
    success_url = reverse_lazy('question_list')
    success_message = 'Question was successfully saved'


class QuestionUpdateView(SuccessMessageMixin, UpdateView):
    model = QuestionVersioned
    form_class = QuestionForm
    template_name = 'questions/question_update.html'
    success_message = 'Question was successfully updated'

    def get_success_url(self):
        self.object.pk
        return reverse('question_answer', kwargs={'pk': self.object.pk})


class QuestionAnswerView(SuccessMessageMixin, CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'questions/question_answer.html'
    success_message = 'Answer was successfully saved'

    def get_success_url(self):
        return reverse('question_answer', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        kwargs['question'] = get_object_or_404(Question, pk=self.kwargs['pk'])
        return super(QuestionAnswerView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.question = get_object_or_404(Question, pk=self.kwargs['pk'])
        if not form.instance.question.actual:
            raise Http404('Question is not loger available for answering')
        return super(QuestionAnswerView, self).form_valid(form)


class OldQuestionsView(TemplateView):
    template_name = 'questions/answer_list.html'

    def get_context_data(self, **kwargs):
        questions = Question.objects.filter(subject_id=self.kwargs['pk'], actual=False).prefetch_related('answer_set')
        return locals()

class TotalAnswersView(TemplateView):
    template_name = 'questions/answer_list.html'

    def get_context_data(self, **kwargs):
        questions = Question.objects.filter(subject_id=self.kwargs['pk'])\
            .prefetch_related('answer_set').order_by('-actual')
        return locals()
