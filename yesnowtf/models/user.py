from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    def display_data(self):

        return {
            'id': self.id,
            'username': self.username,
        }
