from .models import Topic, Subject, SupTopic
from django import forms


class VideoForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"


class SupTopicForm(forms.ModelForm):
    class Meta:
        model = SupTopic
        fields = "__all__"


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"
