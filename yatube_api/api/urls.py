from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/posts/<int:post_id>/comments/',
         CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('v1/posts/<int:post_id>/comments/<int:pk>/',
         CommentViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                'patch': 'partial_update', 'delete': 'destroy'})),
]
