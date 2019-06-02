from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models, serializers


class TypeAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        ret = []
        for item in models.type_choice:
            ret.append({
                'value': item[0],
                'label': item[1]
            })
        return Response(ret)


class UserGroupAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.UserGroupSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)

    def perform_destroy(self, instance):
        for user in instance.users.all():
            user.delete()
        instance.delete()

    def perform_update(self, serializer):
        s = self.get_serializer(data=self.request.data)
        s.is_valid(raise_exception=True)
        data = s.data
        usergroup = self.get_object()
        usergroup.name = data.get('name')
        usergroup.type = data.get('type')
        user_id_list = []
        for user in data.get('users'):
            user_id = user.get('id')
            user_id_list.append(user_id)
        for user in usergroup.users.all():
            if not str(user.id) in user_id_list:
                user.delete()
        for user in data.get('users'):
            user_id = user.get('id')
            if user_id:
                u = models.User.objects.get(id=user_id)
                u.name = user.get('name')
                u.save()
            else:
                u = models.User.objects.create(name=user.get('name'))
                usergroup.users.add(u)
        usergroup.save()

    def get_queryset(self):
        return models.UserGroup.objects.filter(creator=self.request.user)


class UserGroupListCreateAPI(ListCreateAPIView):
    serializer_class = serializers.UserGroupSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = [
        'type'
    ]
    search_fields = [
        'name'
    ]
    ordering_fields = [
        'name',
        'created_datetime',
        'last_modified_datetime'
    ]

    def perform_create(self, serializer):
        data = serializer.validated_data
        usergroup = models.UserGroup.objects.create(
            name=data.get('name'),
            type=data.get('type'),
            creator=self.request.user
        )
        for user in data.get('users'):
            u = models.User.objects.create(name=user.get('name'))
            usergroup.users.add(u)

    def get_queryset(self):
        return models.UserGroup.objects.filter(creator=self.request.user)


class UserGroupListAPI(ListAPIView):
    serializer_class = serializers.UserGroupSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return models.UserGroup.objects.filter(creator=self.request.user)
