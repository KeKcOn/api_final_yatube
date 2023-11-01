from django.urls import path, include

from rest_framework import routers

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowList

router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', PostViewSet)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    'comments',
)
router_v1.register(r'groups', GroupViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/follow/', FollowList.as_view())
]
