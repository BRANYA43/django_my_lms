import time

from django.utils.deprecation import MiddlewareMixin


class DurationRequestProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):

        print('Process request in DurationRequestProcessMiddleware')

        start = time.time()

        response = self.get_response(request)

        print('Process response in DurationRequestProcessMiddleware')

        duration = time.time() - start

        print(f'Duration for track {request.path}: {round(duration, 2)} sec.')

        return response


# class MyMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         print('Precess REQUEST')
#         return request
#
#     def process_response(self, request, response):
#         print('Process Response')
#         return response
#
#
# c = SimpleMiddleware()
# c()
