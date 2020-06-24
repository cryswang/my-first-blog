from django.conf import settings
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Experience(models.Model):
    company = models.CharField(max_length=200, default="company")
    title = models.CharField(max_length=200, default="Intern")
    description =  HTMLField()
    location = models.CharField(max_length=200, default="place, place")
    work_period = models.CharField(max_length=200, default="date - date")
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.company
