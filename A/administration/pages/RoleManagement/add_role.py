from django.shortcuts import render,redirect
from django.views import View
from administration.forms import AddRoleForm
from accounts.models import Role
from django.contrib import messages


class AddRole(View):

    def get(self,request,*args,**kwargs):
        return render(request,"add-role/add-role.html",{
            "section":"مدیریت نقش ها",
            "page":"افزودن نقش جدید",
            "icon":"fa fa-plus-circle",
            "form":AddRoleForm()
        })
    
    def post(self,request,*args,**kwargs):
        form = AddRoleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            add_role_permission_code = 21
            if not request.user.has_permission(add_role_permission_code):
                return redirect("/404")
            role = Role.objects.create(role_name=cd["role_name"])
            role.permissions.set(cd['permissions'])
            messages.success(request,"نقش جدید با موفقیت اضافه شد","success")
            return redirect("administration:role-management")
        return render(request,"add-role/add-role.html",{
            "section":"مدیریت نقش ها",
            "page":"افزودن نقش جدید",
            "icon":"fa fa-plus-circle",
            "form":form
        })