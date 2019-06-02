from rest_framework import generics
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter

from . import models
from . import serializers


class CollectionAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = [
        'name'
    ]
    ordering_fields = [
        'create_datetime'
    ]

    def perform_create(self, serializer):
        data = serializer.validated_data
        collection = models.Collection.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            start_datetime=data.get('start_datetime'),
            end_datetime=data.get('end_datetime'),
            template_file=data.get('template_file'),
            create_datetime=data.get('create_datetime'),
            creator=self.request.user
        )
        for usergroup in data.get('usergroup'):
            collection.usergroup.add(usergroup)

    def get_queryset(self):
        return models.Collection.objects.filter(creator=self.request.user).order_by('create_datetime')

    def get_serializer_class(self):
        if self.request.stream and self.request.stream.method == 'POST':
            return serializers.CollectionSerializer
        else:
            return serializers.CollectionDetailSerializer


class CollectionDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        return models.Collection.objects.filter(creator=self.request.user).order_by('create_datetime')

    def get_serializer_class(self):
        if self.request.stream and self.request.stream.method == 'PUT':
            return serializers.CollectionSerializer
        else:
            return serializers.CollectionDetailSerializer
