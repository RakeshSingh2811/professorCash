from django.urls import path

from . import views

urlpatterns = [
    path("", views.addSubject, name="SubjectForm"),
    path('addSupTopic', views.addSupTopic, name="SupTopicForm"),
    path('addTopic', views.addTopic, name="TopicForm")
]
