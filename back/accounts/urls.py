from django.urls import path
from .views import SignUpView, SignInView

app_name = 'accounts'


urlpatterns = [
    path('signup', SignUpView.as_view()),
    path('login', SignInView.as_view()),
]
