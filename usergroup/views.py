from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import GenericAPIView
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


class UserGroupAPI(GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = serializers.UserGroupSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request)

    def put(self, request, id):
        pass

    def delete(self, request, id):
        pass

    def get_queryset(self):
        return models.UserGroup.objects.filter(creator=self.request.user)


class UserGroupListCreateAPI(GenericAPIView,
                             mixins.CreateModelMixin,
                             mixins.ListModelMixin):
    serializer_class = serializers.UserGroupListSerializer
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

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        return models.UserGroup.objects.filter(creator=self.request.user)

    # def get_serializer_class(self):
    #     pass
