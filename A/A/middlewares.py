from django.http import HttpResponseForbidden
from accounts.models import BlockedIp

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def check_blocked_ip(get_response):
    
    def middleware(request):
        response = get_response(request)
        #return response
        return HttpResponseForbidden('شما توسط ادمین های سایت بلاک شده اید') if BlockedIp.objects.filter(ip=get_client_ip(request)).first() else response

    return middleware