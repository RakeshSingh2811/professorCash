from django.db import models
# Create your models here


class Subject(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class SupTopic(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=500)
    video = models.FileField(upload_to="videos/", null=True, verbose_name="")
    description = models.TextField()
    supTopic = models.ForeignKey(SupTopic, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
