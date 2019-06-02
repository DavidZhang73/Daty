import time

from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response

from utils.models import UploadFile


class UploadFileAPI(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        file = request.FILES['file']
        filename = file.name
        file.name = f'{int(time.time())}_{filename}'
        f = UploadFile.objects.create(
            name=filename,
            file=file,
            uploader=request.user
        )
        return Response({
            'id': f.id,
            'url': f.get_url()
        })
