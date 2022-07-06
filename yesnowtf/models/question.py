from django.db import models
from django.utils import timezone


class Question(models.Model):

    created_at = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    author = models.ForeignKey('User', related_name='questions', on_delete=models.CASCADE)

    def display_data(self):

        data = {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'text': self.text,
            'author': self.author.display_data(),
        }

        return data
