import uuid

from django.db import models

class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class Logs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contentId = models.UUIDField(editable=False, null=False)
    todo = models.OneToOneField(
        Todo,
        on_delete=models.CASCADE,
        related_name='log'
    )

class TodoDetailed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=200, null=True)
    isPinned = models.BooleanField(default=False)
    completedAt = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(
        max_length=20,
        choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
            ('urgent', 'Urgent'),
        ],
        default='low'
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('in_progress', 'In Progress'),
            ('completed', 'Completed'),
            ('overdue', 'Overdue'),
        ],
        default='pending'
    )

    todo = models.OneToOneField(
        Todo,
        on_delete=models.CASCADE,
        related_name='details'
    )

class TodoHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    todo = models.ForeignKey(
        Todo,
        on_delete=models.CASCADE,
        related_name='history'
    )
    action = models.CharField(max_length=200)  # e.g. "marked completed", "updated title"
    timestamp = models.DateTimeField(auto_now_add=True)