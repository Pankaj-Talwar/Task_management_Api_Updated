from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class Custom(AbstractUser):
    USER_TYPES = [
        ('manager', 'Manager'),
        ('developer', 'Developer'),
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    custom_groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_groups')
    
    # Update related_name for user_permissions
Custom._meta.get_field('user_permissions').related_name = 'custom_user_permissions'

class Task(models.Model):
    STATUS_CHOICES = [
        ('Todo', 'Todo'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]

    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Todo')
    assigned_to = models.ForeignKey(Custom, on_delete=models.CASCADE, related_name='assigned_tasks')
    created_by = models.ForeignKey(Custom, on_delete=models.CASCADE, related_name='created_tasks')
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    user = models.ForeignKey(Custom, on_delete=models.CASCADE, related_name='comments')  # Update related_name
    created_at = models.DateTimeField(auto_now_add=True)
