from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename='project')
router.register(r'tasks', views.TaskViewSet, basename='task')
router.register(r'comments', views.CommentViewSet, basename='comment')
router.register(r'projectmembers', views.ProjectMemberViewSet, basename='projectmember')

urlpatterns = [
    path('users/register/', views.register_user, name='register_user'),
    path('users/login/', views.login_user, name='login_user'),
    path('', include(router.urls)),
]
