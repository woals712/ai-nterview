from django.db import models
# django github에서 AbstractUser 클래스 확인 가능
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 추후 User Model 확장을 위해 미리 AbstractUser 상속 받아 정의


class User(AbstractUser):
    pass


class Meta:
    db_table = "accounts"
