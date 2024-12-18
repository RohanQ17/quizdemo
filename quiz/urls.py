from django.urls import path
from .import views

urlpatterns = [
       path('', views.home, name='home'),
       path('start-quiz/', views.start_quiz, name='start_quiz'),
       path('quiz/', views.quiz_question, name='quiz_question'),
       path('submit-answer/', views.submit_answer, name='submit_answer'),
       path('result/', views.quiz_result, name='quiz_result'),
]