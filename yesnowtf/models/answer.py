from django.db import models
from django.utils import timezone


class Answer(models.Model):

    class AnswerText(models.TextChoices):
        YES = 'yes'
        NO = 'no'

    created_at = models.DateTimeField(default=timezone.now)
    text = models.TextField(choices=AnswerText.choices)
    question = models.OneToOneField('Question', related_name='answer', on_delete=models.PROTECT)

    def display_data(self, is_full=False):

        data = {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'text': self.text,
        }

        if is_full:
            data['question'] = self.question.display_data()

        return data
