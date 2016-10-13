from django.db import models
from django.db import transaction


class CreatedAtFormatMixin(object):
    def get_created_at(self, fmt="%d/%m/%y %H:%M"):
        return self.created_at.strftime(fmt)


class Subject(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pk


class Question(CreatedAtFormatMixin, models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    actual = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255)
    edit_count = models.PositiveIntegerField(default=0)
    answer_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return "%d %s" % (self.subject_id, self.text)


class QuestionVersioned(Question):
    class Meta:
        proxy = True

    @transaction.atomic
    def save(self):
        if self.pk:
            Question.objects.filter(subject_id=self.subject_id).update(actual=False)
            self.pk = None
            self.created_at = None
            self.actual = True
            self.edit_count += 1
        else:
            subject = Subject()
            subject.save()
            self.subject = subject
        return super(QuestionVersioned, self).save()


class Answer(CreatedAtFormatMixin, models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255)

    class Meta:
        ordering = ["created_at"]

    @transaction.atomic
    def save(self):
        if not self.pk:
            self.question.answer_count += 1
            self.question.save()
        return super(Answer, self).save()

    def __str__(self):
        return "%d %s" % (self.question_id, self.text)