from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # change key name to error
    if response is not None:
        if response.data.get('detail'):
            response.data['error'] = response.data.pop('detail')
    else:
        response = Response({'error': exc.args[0]}, status=500)
    return response
