from django.urls import path
from aws_app import views

urlpatterns = [
    path('aws_app/', views.aws_List.as_view()),
]