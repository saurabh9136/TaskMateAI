from django.contrib.auth.models import User
from django.db import models

class AIResponse(models.Model):
    ai_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.ai_text[:50]

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Make user optional
    task_title = models.CharField(max_length=50)
    task_description = models.TextField()
    status = models.IntegerField(default=0)  # 0 = pending, 1 = completed
    ai_response = models.OneToOneField(AIResponse, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.task_title
