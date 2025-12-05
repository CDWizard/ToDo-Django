import uuid

from django.db import models

class Todo(models.Model):
    id = models.CharField(primary_key=True, default=str(uuid.uuid4()), max_length=36)
    title = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class Logs(models.Model):
    contentId = models.CharField(max_length=36)