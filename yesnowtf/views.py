from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from yesnowtf.serializers import QuestionSerializer
from yesnowtf.services import AnswerService


class QuestionView(APIView):

    def post(self, request):

        serializer = QuestionSerializer(data=request.data)

        if serializer.is_valid():

            question = serializer.save(author=request.user)
            answer = AnswerService.create_answer(question=question)

            data = {
                'question_info': question.display_data(),
                'answer_info': answer,
            }

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

