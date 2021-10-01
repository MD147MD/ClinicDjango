from django.shortcuts import render,redirect
from django.views import View
from administration.forms import AddCategoryForm
from accounts.models import Category
from django.contrib import messages
from uuid import UUID

# Note : we used AddCategoryForm instead if EditCategoryForm because the operations are same

class EditCategory(View):

    def get(self,request,category_id,*args,**kwargs):
        category = None
        try:
            category_id = UUID(category_id)
            category = Category.objects.get(pk=category_id)
        except:
            return redirect("/404")

        return render(request,"edit-category/edit-category.html",{
            "section":"مدیریت دسته ها",
            "page":"ویرایش دسته",
            "icon":"fa fa-pencil",
            "form":AddCategoryForm(initial={"category_name":category.category_name}),
            "category":category
        })
    
    def post(self,request,category_id,*args,**kwargs):
        category = None
        try:
            category_id = UUID(category_id)
            category = Category.objects.get(pk=category_id)
        except:
            return redirect("/404")

        form = AddCategoryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            edit_category_permission_code = 42
            if not request.user.has_permission(edit_category_permission_code):
                return redirect("/404")
            category.category_name = cd['category_name']
            category.save()
            messages.success(request,"دسته مورد نظر با موفقیت ویرایش شد","success")
            return redirect("administration:category-management")
        return render(request,"edit-category/edit-category.html",{
            "section":"مدیریت دسته ها",
            "page":"ویرایش دسته",
            "icon":"fa fa-pencil",
            "form":form
        })