from django.shortcuts import render,redirect
from django.views import View
from administration.forms import AddSubCategoryForm
from accounts.models import SubCategory,Category
from django.contrib import messages
from uuid import UUID


class AddSubCategory(View):

    def get(self,request,category_id,*args,**kwargs):
        category = None
        try:
            category_id = UUID(category_id)
            category = Category.objects.get(pk=category_id)
        except:
            return redirect("/404")
        return render(request,"add-sub-category/add-sub-category.html",{
            "section":"مدیریت دسته ها",
            "page":"افزودن زیر دسته جدید",
            "icon":"fa fa-plus-circle",
            "form":AddSubCategoryForm()
        })
    
    def post(self,request,category_id,*args,**kwargs):
        category = None
        try:
            category_id = UUID(category_id)
            category = Category.objects.get(pk=category_id)
        except:
            return redirect("/404")

        form = AddSubCategoryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            add_category_permission_code = 41
            if not request.user.has_permission(add_category_permission_code):
                return redirect("/404")
            sub_category = SubCategory.objects.create(sub_category_name=cd["sub_category_name"],parent_category=category)
            messages.success(request,"زیر دسته جدید با موفقیت اضافه شد","success")
            return redirect("administration:category-management")
        return render(request,"add-sub-category/add-sub-category.html",{
            "section":"مدیریت دسته ها",
            "page":"افزودن زیر دسته جدید",
            "icon":"fa fa-plus-circle",
            "form":form
        })