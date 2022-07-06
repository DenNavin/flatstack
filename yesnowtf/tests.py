from django.test import TestCase

from rest_framework.test import APIClient

from yesnowtf.conf import StatusCode
from yesnowtf.models import Question, Answer, User
from yesnowtf.services import AnswerService
from yesnowtf.utils import get_answer_info


class TestCaseQuestion(TestCase):

    username = 'test_user'
    url = 'http://127.0.0.1:8000/ynw/question/'

    def setUp(self):
        User.objects.create(username=self.username)

    def test_create_full_data(self):
        client = APIClient()
        user = User.objects.get(username=self.username)

        data = {'text': 'test2'}
        client.force_authenticate(user)
        response = client.post(path=self.url, data=data)

        self.assertEquals(Question.objects.count(), 1)
        self.assertEquals(Answer.objects.count(), 1)
        self.assertEquals(response.status_code, 201)

    def test_create_without_auth(self):
        client = APIClient()
        data = {'text': 'test2'}

        response = client.post(path=self.url, data=data)

        self.assertEquals(Question.objects.count(), 0)
        self.assertEquals(Answer.objects.count(), 0)
        self.assertEquals(response.status_code, 401)

    def test_create_without_data(self):
        client = APIClient()
        user = User.objects.get(username=self.username)

        data = {}
        client.force_authenticate(user)
        response = client.post(path=self.url, data=data)

        self.assertEquals(Question.objects.count(), 0)
        self.assertEquals(Answer.objects.count(), 0)
        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.json()['text'], ['This field is required.'])


class TestCaseAnswer(TestCase):

    username = 'test_user'

    def setUp(self):
        user = User.objects.create(username=self.username)
        Question.objects.create(text='test2', author=user)

    def test_create_answer(self):
        question = Question.objects.get(text='test2')
        answer = AnswerService.create_answer(question=question)

        self.assertEquals(Answer.objects.count(), 1)
        self.assertIn(answer['text'], [Answer.AnswerText.YES, Answer.AnswerText.NO])

    def test_get_answer_info(self):

        answer_info = get_answer_info()

        self.assertEquals(answer_info['status'], StatusCode.OK)
        self.assertIn(answer_info['answer_info']['answer'], [Answer.AnswerText.YES, Answer.AnswerText.NO])
