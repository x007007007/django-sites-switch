try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    class MiddlewareMixin(object):
        pass
import logging
import threading
import weakref


logger = logging.getLogger(__name__)
_requests = weakref.WeakKeyDictionary()


class RecordRequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request_id = id(request)
        logger.debug("process_request: arg {}".format(request_id))
        _requests[threading.currentThread()] = (request,)


class RidRecordRequestMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        logger.debug("process_response: arg {}".format(id(request)))
        del _requests[threading.currentThread()]
        return response


class RecordAndRidRequestMiddleware(RecordRequestMiddleware, RidRecordRequestMiddleware):
    pass


def get_request():
    if _requests and threading.currentThread() in _requests:
        return _requests[threading.currentThread()][0]
    return None