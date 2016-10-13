from unittest.mock import patch
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from mixer.backend.django import mixer
import pytest

from .views import QuestionListView, QuestionCreateView, QuestionAnswerView
from .models import Subject, Question, Answer

pytestmark = pytest.mark.django_db


class TestViews(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s1 = mixer.blend(Subject)
        cls.q1 = mixer.blend(Question, subject=cls.s1, actual=False)
        cls.a11 = mixer.blend(Answer, question=cls.q1)
        cls.a12 = mixer.blend(Answer, question=cls.q1)

        cls.q2 = answer = mixer.blend(Question, subject=cls.s1, actual=False)
        cls.a21 = mixer.blend(Answer, question=cls.q2)
        cls.a22 = mixer.blend(Answer, question=cls.q2)

        cls.q3 = answer = mixer.blend(Question, subject=cls.s1, actual=True)
        cls.a31 = mixer.blend(Answer, question=cls.q3)
        cls.a32 = mixer.blend(Answer, question=cls.q3)

        return super(TestViews, cls).setUpClass()

    def test_list(self):
        req = RequestFactory().get(reverse('question_list'))
        resp = QuestionListView.as_view()(req)
        resp.render()
        assert resp.status_code == 200, 'List is working'

    def test_question_create(self):
        req = RequestFactory().get(reverse('question_create'))
        resp = QuestionCreateView.as_view()(req)
        resp.render()
        assert resp.status_code == 200, 'Create is working'

    def test_question_update(self):
        kwargs = {'pk': self.q3.pk}
        url = reverse('question_update', kwargs=kwargs)
        req = RequestFactory().get(url)
        resp = QuestionCreateView.as_view()(req, **kwargs)
        resp.render()
        assert resp.status_code == 200, 'Update is working'

    def test_question_answer(self):
        kwargs = {'pk': self.q3.pk}
        url = reverse('question_answer', kwargs=kwargs)
        req = RequestFactory().get(url)
        resp = QuestionAnswerView.as_view()(req, **kwargs)
        resp.render()
        assert resp.status_code == 200, 'Answer form is working'
