from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class AuthMiddelWare(MiddlewareMixin):

    def process_request(self, request):
        if request.path_info in ['/login/', '/image/code/']:
            return

        info = request.session.get('info')
        if info:
            return
        else:
            return redirect('/login/')
