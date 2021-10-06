from django.views import View
from uuid import UUID
from accounts.models import Role
from django.shortcuts import redirect
from django.contrib import messages


class RemoveRole(View):

    def get(self,request,role_id,*args,**kwargs):
        role = None
        try:
            role_id = UUID(role_id)
            role = Role.objects.get(pk=role_id)
        except:
            return redirect("/404")
        remove_role_permission_code = 23
        if not request.user.has_permission(remove_role_permission_code):
            return redirect("/404")
        role.is_removed = True
        role.save()
        messages.success(request,"نقش مورد نظر با موفقیت حذف شد","success")
        return redirect("administration:role-management")