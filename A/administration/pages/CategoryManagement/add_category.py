from django.shortcuts import render,redirect
from django.views import View
from administration.forms import AddCategoryForm
from accounts.models import Category
from django.contrib import messages


class AddCategory(View):

    def get(self,request,*args,**kwargs):
        return render(request,"add-category/add-category.html",{
            "section":"مدیریت دسته ها",
            "page":"افزودن دسته جدید",
            "icon":"fa fa-plus-circle",
            "form":AddCategoryForm()
        })
    
    def post(self,request,*args,**kwargs):
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            add_category_permission_code = 41
            if not request.user.has_permission(add_category_permission_code):
                return redirect("/404")
            category = Category.objects.create(category_name=cd["category_name"])
            messages.success(request,"دسته جدید با موفقیت اضافه شد","success")
            return redirect("administration:category-management")
        return render(request,"add-category/add-category.html",{
            "section":"مدیریت دسته ها",
            "page":"افزودن دسته جدید",
            "icon":"fa fa-plus-circle",
            "form":form
        })