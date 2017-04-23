try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    class MiddlewareMixin(object):
        pass
import logging
import threading


logger = logging.getLogger(__name__)
_thread_local = threading.local()


class RecordRequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        logger.debug("process_request: arg {}".format(id(request)))
        _thread_local._request = request


class RidRecordRequestMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        logger.debug("process_response: arg {}".format(id(request)))
        del _thread_local._request
        return response


class RecordAndRidRequestMiddleware(RecordRequestMiddleware, RidRecordRequestMiddleware):
    pass


def get_request():
    return getattr(_thread_local, "_request", None)
