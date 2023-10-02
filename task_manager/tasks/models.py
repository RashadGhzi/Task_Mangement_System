from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    PRIORIY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    photos = models.ImageField(upload_to='task_photos/')
    creation_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORIY_CHOICES, default='medium')
    is_complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['priority']