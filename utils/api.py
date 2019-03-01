from collections import OrderedDict

from rest_framework.views import APIView
from rest_framework.response import Response


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

    def _serializer_error_to_str(self, errors):
        for k, v in errors.items():
            if isinstance(v, list):
                return k, v[0]
            elif isinstance(v, OrderedDict):
                for _k, _v in v.items():
                    return self._serializer_error_to_str({_k: _v})

    def invalid_serializer(self, serializer):
        k, v = self._serializer_error_to_str(serializer.errors)
        if k != "non_field_errors":
            return self.error()
        else:
            return self.error()
