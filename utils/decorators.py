import functools


def validate_serializer(serializer):
    """
    @validate_serializer(TestSerializer)
    def post(self, request):
        return self.success(request.data)
    """

    def validate(view_method):
        @functools.wraps(view_method)
        def handle(*args, **kwargs):
            self = args[0]
            request = args[1]
            s = serializer(data=request.data)
            if s.is_valid():
                request.validated_data = s.data
                request.serializer = s
                return view_method(*args, **kwargs)
            else:
                return self.error(s.errors)

        return handle

    return validate
