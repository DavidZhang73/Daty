from rest_framework import generics
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import get_object_or_404
from . import models
from . import serializers


class CollectionAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = [
        'name'
    ]
    ordering_fields = [
        'created_datetime'
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
            ug = get_object_or_404(models.UserGroup, id=usergroup)
            collection.usergroup.add(ug)

    def get_queryset(self):
        return models.Collection.objects.filter(creator=self.request.user)

    def get_serializer_class(self):
        if self.request.stream and self.request.stream.method == 'POST':
            return serializers.CollectionSerializer
        else:
            return serializers.CollectionDetailSerializer
