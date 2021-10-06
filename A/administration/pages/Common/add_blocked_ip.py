from django.shortcuts import render,redirect
from django.views import View
from administration.forms import AddBlockedIpForm
from accounts.models import BlockedIp
from django.contrib import messages


class AddBlockedIp(View):

    def get(self,request,*args,**kwargs):
        return render(request,"add-blocked-ip/add-blocked-ip.html",{
            "section":"مدیریت آیپی بلاک شده ها",
            "page":"افزودن آیپی بلاک شده جدید",
            "icon":"fa fa-plus-circle",
            "form":AddBlockedIpForm()
        })
    
    def post(self,request,*args,**kwargs):
        form = AddBlockedIpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            add_blocked_ip_permission_code = 81
            if not request.user.has_permission(add_blocked_ip_permission_code):
                return redirect("/404")
            blocked_ip = BlockedIp.objects.create(ip=cd["ip"]).save()
            messages.success(request,"آیپی بلاک شده جدید با موفقیت اضافه شد","success")
            return redirect("administration:ip-management")
        return render(request,"add-blocked_ip/add-blocked_ip.html",{
            "section":"مدیریت آیپی بلاک شده ها",
            "page":"افزودن آیپی بلاک شده جدید",
            "icon":"fa fa-plus-circle",
            "form":form
        })