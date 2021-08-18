

class SampleMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):

        print('before view')
        request.abcd = 'javas'

        response = self.get_response(request)
        response.aaa = 'nnnnnn'

        print('after view')

        return response


class SampleMiddleware2:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):

        print('before view2')

        response = self.get_response(request)

        print('after view2')

        return response