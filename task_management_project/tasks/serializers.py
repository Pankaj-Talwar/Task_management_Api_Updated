# tasks/serializers.py
from rest_framework import serializers
from .models import Custom, Task, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom
        fields = ['id', 'username', 'user_type']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'text', 'user', 'created_at']

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer()
    created_by = UserSerializer()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'status', 'assigned_to', 'created_by', 'created_at', 'comments']
