from django.shortcuts import render,redirect
from django.views import View
from administration.forms import AddSubCategoryForm
from accounts.models import SubCategory
from django.contrib import messages
from uuid import UUID


# None : We used AddSubCategoryForm instead of create EditSubCategoryForm because their operations are same

class EditSubCategory(View):

    def get(self,request,sub_category_id,*args,**kwargs):
        sub_category = None
        try:
            sub_category_id = UUID(sub_category_id)
            sub_category = SubCategory.objects.get(pk=sub_category_id)
        except:
            return redirect("/404")
        return render(request,"edit-sub-category/edit-sub-category.html",{
            "section":"مدیریت دسته ها",
            "page":"ویرایش زیر دسته ",
            "icon":"fa fa-pencil",
            "form":AddSubCategoryForm(initial={'sub_category_name':sub_category.sub_category_name})
        })
    
    def post(self,request,sub_category_id,*args,**kwargs):
        sub_category = None
        try:
            sub_category_id = UUID(sub_category_id)
            sub_category = SubCategory.objects.get(pk=sub_category_id)
        except:
            return redirect("/404")

        form = AddSubCategoryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            edit_category_permission_code = 42
            if not request.user.has_permission(edit_category_permission_code):
                return redirect("/404")
            sub_category.sub_category_name = cd["sub_category_name"]
            sub_category.save()
            messages.success(request,"زیر دسته با موفقیت ویرایش شد","success")
            return redirect("administration:category-management")
        return render(request,"edit-sub-category/edit-sub-category.html",{
            "section":"مدیریت دسته ها",
            "page":"ویرایش زیر دسته ",
            "icon":"fa fa-pencil",
            "form":form
        })