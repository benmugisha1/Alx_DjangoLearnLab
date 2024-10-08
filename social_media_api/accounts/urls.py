from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/<int:pk>/follow/', UserViewSet.as_view({'post': 'follow'})),
    path('users/<int:pk>/unfollow/', UserViewSet.as_view({'post': 'unfollow'})),
]
from django.urls import path
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('users/<int:pk>/follow/', FollowUserView.as_view(), name='follow_user'),
    path('users/<int:pk>/unfollow/', UnfollowUserView.as_view(), name='unfollow_user'),
]

from django.urls import path
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    # Other URL patterns can be added here

    # Route for following a user
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),

    # Route for unfollowing a user
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]
