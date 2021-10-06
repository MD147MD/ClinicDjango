from django.views import View
from uuid import UUID
from accounts.models import BlockedIp
from django.shortcuts import redirect
from django.contrib import messages


class RemoveBlockedIp(View):

    def get(self,request,id,*args,**kwargs):
        blocked_ip = None
        try:
            blocked_ip_id = UUID(id)
            blocked_ip = BlockedIp.objects.get(pk=blocked_ip_id)
        except:
            return redirect("/404")
        remove_blocked_ip_permission_code = 83
        if not request.user.has_permission(remove_blocked_ip_permission_code):
            return redirect("/404")
        blocked_ip.is_removed = True
        blocked_ip.save()
        messages.success(request,"آیپی بلاک شده مورد نظر با موفقیت حذف شد","success")
        return redirect("administration:ip-management")