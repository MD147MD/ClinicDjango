from django.shortcuts import render,redirect
from django.views import View
from administration.forms import AddRoleForm
from accounts.models import Role
from django.contrib import messages
from uuid import UUID

# Note: in here we used AddRoleForm Instead of Creating EditRoleForm Because the forms are same

class EditRole(View):

    def get(self,request,role_id,*args,**kwargs):
        role = None
        try:
            role_id = UUID(role_id)
            role = Role.objects.get(pk=role_id)
        except:
            return redirect("/404")

        return render(request,"edit-role/edit-role.html",{
            "section":"مدیریت نقش ها",
            "page":"ویرایش نقش",
            "icon":"fa fa-pencil-square",
            "form":AddRoleForm(initial={"role_name":role.role_name,"permissions":list(role.permissions.all().values_list("id",flat=True))})
        })
    
    def post(self,request,role_id,*args,**kwargs):

        role = None
        try:
            role_id = UUID(role_id)
            role = Role.objects.get(pk=role_id)
        except:
            return redirect("/404")
        form = AddRoleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            edit_role_permission_code = 22
            if not request.user.has_permission(edit_role_permission_code):
                return redirect("/404")
            role.role_name = cd['role_name']
            role.save()
            role.permissions.set(cd['permissions'])
            messages.success(request,"نقش مورد نظر با موفقیت ویرایش شد","success")
            return redirect("administration:role-management")
        return render(request,"edit-role/edit-role.html",{
            "section":"مدیریت نقش ها",
            "page":"ویرایش نقش",
            "icon":"fa fa-pencil-square",
            "form":form
        })