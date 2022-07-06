from rest_framework import serializers

from yesnowtf.models import Question


class QuestionSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, allow_blank=True, max_length=100)

    def create(self, validated_data):
        author = validated_data.get('author', None)

        return Question.objects.create(**validated_data)
