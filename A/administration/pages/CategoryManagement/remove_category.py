from django.views import View
from uuid import UUID
from accounts.models import Category
from django.shortcuts import redirect
from django.contrib import messages


class RemoveCategory(View):

    def get(self,request,category_id,*args,**kwargs):
        category = None
        try:
            category_id = UUID(category_id)
            category = Category.objects.get(pk=category_id)
        except:
            return redirect("/404")
        category.is_removed = True
        category.save()
        messages.success(request,"دسته مورد نظر با موفقیت حذف شد","success")
        return redirect("administration:category-management")