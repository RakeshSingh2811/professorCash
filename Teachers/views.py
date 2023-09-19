from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, SupTopic, Subject
from .form import VideoForm, SubjectForm, SupTopicForm


def addTopic(request):
    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "Teachers/index.html", context)


def addSupTopic(request):
    form = SupTopicForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }
    return render(request, "Teachers/index.html", context)


def addSubject(request):
    form = SubjectForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }
    return render(request, "Teachers/index.html", context)
