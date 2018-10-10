from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializers import UserSerializer, QuestionSerializer
from polls.models import Question


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

