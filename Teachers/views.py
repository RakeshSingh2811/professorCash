from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, SupTopic, Subject
from .form import VideoForm, SubjectForm, SupTopicForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def addTopic(request):
    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
        'heading': "Add Topic"
    }
    return render(request, "Teachers/index.html", context)


@csrf_exempt
def addSupTopic(request):
    form = SupTopicForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form,
        'heading': "Add Super Topic"
    }
    return render(request, "Teachers/index.html", context)


@csrf_exempt
def addSubject(request):
    form = SubjectForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form,
        'heading': "Add Subject"
    }
    return render(request, "Teachers/index.html", context)


def viewTopics(request):
    topics = Topic.objects.all()
    return render(request, "Teachers/list.html", {"topics": topics})
