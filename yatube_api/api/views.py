from collections import OrderedDict

from django.shortcuts import get_object_or_404

from rest_framework import viewsets, permissions, filters
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from posts.models import Post, Group, Follow, User
from .serializers import (
    PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer)
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthorOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_paginated_response(self, data):
        if ('limit' in self.request.query_params
                and 'offset' in self.request.query_params):
            return Response(OrderedDict([
                ('count', self.paginator.count),
                ('next', self.paginator.get_next_link()),
                ('previous', self.paginator.get_previous_link()),
                ('results', data)
            ]))
        return Response(data)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        queryset = post.comments.all()
        return queryset


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def perform_create(self, serializer):
        following = self.request.data.get('following')
        if not following:
            raise ValidationError({'following': ['This field is required.']})
        following_user = get_object_or_404(User, username=following)
        if Follow.objects.filter(
                user=self.request.user,
                following=following_user,
        ).exists():
            raise ValidationError(
                {'following': ['You are already following this user.']})
        if following_user == self.request.user:
            raise ValidationError({'following': ['You cant sign yourself.']})
        serializer.save(user=self.request.user, following=following_user)

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        return queryset
