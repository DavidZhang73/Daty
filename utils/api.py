from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response


class APIViewSet(GenericViewSet):
    def response(self, data):
        return Response(data)

    def success(self, data):
        return self.response({
            'error': '',
            'data': data
        })

    def error(self, error):
        return self.response({
            'error': error,
            'data': ''
        })


class API(APIView):
    def response(self, data):
        return Response(data)

    def success(self, data):
        return self.response({
            'error': '',
            'data': data
        })

    def error(self, error):
        return self.response({
            'error': error,
            'data': ''
        })
