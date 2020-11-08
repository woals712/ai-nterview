import json

from .models import User

from django.views import View
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            # 존재하는 이메일인지 확인
            if User.objects.filter(email=data['email']).exists():
                return HttpResponse(status=400)

            User(
                name=data['name'],
                email=data['email'],
                password=data['password']
            ).save()

            return HttpResponse(status=200)
        except KeyError:
            return JsonResponse({"message": "INVALID_KEYS"}, status=400)


class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        if User.objects.filter(email=data['email']).exists():
            user = User.objects.get(email=data['email'])
            if user.password == data['password']:
                return JsonResponse({'message': '로그인 성공!'}, status=200)
            else:
                return JsonResponse({'message': '비밀번호가 틀렸어요'}, status=200)

        return JsonResponse({'message': '등록되지 않은 이메일 입니다.'}, status=200)
