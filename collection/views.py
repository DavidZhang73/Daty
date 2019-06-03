from rest_framework import generics
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter

from . import models
from . import serializers


class CollectionAPI(generics.ListCreateAPIView):
    """
    获得文件集列表
    新建文件集
    """
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
            for user in usergroup.users.all():
                models.CollectionFile.objects.create(
                    collection=collection,
                    uploader=user
                )

    def get_queryset(self):
        return models.Collection.objects.filter(creator=self.request.user).order_by('create_datetime')

    def get_serializer_class(self):
        if self.request.stream and self.request.stream.method == 'POST':
            return serializers.CollectionSerializer
        else:
            return serializers.CollectionDetailSerializer


class CollectionDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    获得指定文件集
    更改指定文件集
    删除指定文件集
    """
    lookup_field = 'pk'

    def get_queryset(self):
        return models.Collection.objects.all().order_by('create_datetime')

    def get_serializer_class(self):
        if self.request.stream and self.request.stream.method == 'PUT':
            return serializers.CollectionSerializer
        else:
            return serializers.CollectionDetailSerializer


class CollectionFileAPI(generics.ListAPIView):
    """
    获得文件集文件列表
    """
    serializer_class = serializers.CollectionFileDetailSerializer
    pagination_class = None

    def get_queryset(self):
        collection_id = self.request.query_params.get('collection_id')
        return models.CollectionFile.objects.filter(collection_id=collection_id)


class CollectionFileUploadAPI(generics.UpdateAPIView):
    """
   文件集文件上传
    """
    serializer_class = serializers.CollectionFileUploadSerializer
    queryset = models.CollectionFile.objects.all()
    lookup_field = 'pk'
