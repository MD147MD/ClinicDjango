from django.views import View
from uuid import UUID
from accounts.models import SubCategory
from django.shortcuts import redirect
from django.contrib import messages


class RemoveSubCategory(View):

    def get(self,request,sub_category_id,*args,**kwargs):
        sub_category = None
        try:
            sub_category_id = UUID(sub_category_id)
            sub_category = SubCategory.objects.get(pk=sub_category_id)
        except:
            return redirect("/404")
        remove_category_permission_code = 43
        if not request.user.has_permission(remove_category_permission_code):
            return redirect("/404")
        sub_category.is_removed = True
        sub_category.save()
        messages.success(request,"زیردسته مورد نظر با موفقیت حذف شد","success")
        return redirect("administration:category-management")