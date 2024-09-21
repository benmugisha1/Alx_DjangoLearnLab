from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path
from .views import FeedView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
]
