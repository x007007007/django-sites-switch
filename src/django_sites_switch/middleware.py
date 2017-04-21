try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    class MiddlewareMixin(object):
        pass


_request = []


class RecordRequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
         _request.append(request)


    def process_response(self, request, response):
        _request.pop()
        return response


def get_request():
    if _request:
        return _request[0]
    return None