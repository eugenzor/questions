from django.conf.urls import url
from django.contrib import admin

from django.views.generic import TemplateView

from .views import QuestionListView, QuestionCreateView, QuestionUpdateView, QuestionAnswerView, \
    OldQuestionsView, TotalAnswersView

urlpatterns = [
    url(r'^$', QuestionListView.as_view(), name='question_list'),
    url(r'^create/$', QuestionCreateView.as_view(), name='question_create'),
    url(r'^update/(?P<pk>[0-9]+)/$', QuestionUpdateView.as_view(), name='question_update'),
    url(r'^answer/(?P<pk>[0-9]+)/$', QuestionAnswerView.as_view(), name='question_answer'),
    url(r'^old-questions/(?P<pk>[0-9]+)/$', OldQuestionsView.as_view(), name='old_questions'),
    url(r'^total-answers/(?P<pk>[0-9]+)/$', TotalAnswersView.as_view(), name='total_answers'),

    url(r'^admin/', admin.site.urls),
]
