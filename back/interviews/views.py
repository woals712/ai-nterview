from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Question, Category
from .serializers import QuestionSerializer

# Create your views here.

User = get_user_model()


@api_view(['GET'])
def questions_list(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def questions_create(request):
    try:
        category = Category.objects.get(category=request.user.username)

    except:
        category = Category.objects.create(category=request.user.username)

    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(category=category)
        return Response(serializer.data)
    return Response(status=400)


@api_view(['DELETE'])
def questions_delete(request):
    question = get_object_or_404(Question, id=id)
    question.delete()
    return Response("delete success")
