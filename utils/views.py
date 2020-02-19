import time
import zipfile
from io import BytesIO

from django.http.response import HttpResponse
from rest_framework import views
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from collection.models import CollectionFile
from utils.models import UploadFile


class UploadFileAPI(views.APIView):

    def post(self, request):
        file = request.FILES['file']
        filename = file.name
        file.name = f'{int(time.time())}_{filename}'
        f = UploadFile.objects.create(
            name=filename,
            file=file,
        )
        if request.user.is_authenticated:
            f.uploader = request.user
            f.save()
        return Response({
            'id': f.id,
            'url': f.get_url()
        })


class DownloadAllCollectionFileAPI(views.APIView):
    def get(self, request):
        collection_id = request.query_params.get('collection_id')
        collection_file_list = CollectionFile.objects.filter(collection_id=collection_id)
        file_list = []
        try:
            for collection_file in collection_file_list:
                if collection_file.file:
                    file_list.append(collection_file.file.file)
            zip = BytesIO()
            with zipfile.ZipFile(zip, 'w', zipfile.ZIP_DEFLATED) as zf:
                for file in file_list:
                    with open(file.path, 'rb') as f:
                        zf.writestr(str(file), f.read())
        except Exception as e:
            raise APIException(e)
        return HttpResponse(zip.getvalue(), content_type="application/zip")
