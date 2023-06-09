from django.db import models
from django.utils import timezone


class TodoItem(models.Model):
    username = models.CharField(max_length=50, default='User')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    deadline_at = models.DateTimeField(null=False, blank=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
