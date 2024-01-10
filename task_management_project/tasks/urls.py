from django.urls import path
from .views import TaskListCreateView, TaskDetailView, CommentListCreateView, CommentDetailView
from rest_framework.routers import DefaultRouter
# from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskListCreateView, basename='task')

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
