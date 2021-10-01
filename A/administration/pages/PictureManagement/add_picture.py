from django.shortcuts import render,redirect
from django.views import View
from administration.forms import AddPictureForm
from pictures.models import ClinicPicture
from django.contrib import messages


class AddPicture(View):

    def get(self,request,*args,**kwargs):
        return render(request,"add-picture/add-picture.html",{
            "section":"مدیریت عکس ها",
            "page":"افزودن عکس جدید",
            "icon":"fa fa-plus-circle",
            "form":AddPictureForm()
        })

    def post(self,request,*args,**kwargs):
        form = AddPictureForm(request.POST,request.FILES)
        add_picture_permission_code = 31
        if not request.user.has_permission(add_picture_permission_code):
            return redirect("/404")
        if form.is_valid():
            cd = form.cleaned_data
            ClinicPicture.objects.create(picture_title=cd['picture_title'],picture=cd['picture'])
            messages.success(request,"عکس جدید با موفقیت اضافه شد","success")
            return redirect("administration:picture-management")
        return render(request,"add-picture/add-picture.html",{
            "section":"مدیریت عکس ها",
            "page":"افزودن عکس جدید",
            "icon":"fa fa-plus-circle",
            "form":form
        })