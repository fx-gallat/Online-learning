from django.urls import path
from . import views

urlpatterns = [
    path('questions', views.QuestionList.as_view()),
    path('question/(?P<pk>[0-9]+)$', views.QuestionDetail.as_view()),
]