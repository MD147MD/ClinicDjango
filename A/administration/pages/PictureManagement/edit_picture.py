from django.shortcuts import render,redirect
from django.views import View
from administration.forms import AddPictureForm
from pictures.models import ClinicPicture
from uuid import UUID
from django.contrib import messages
# Note : we used AddPictureForm Instead of createing EditPictureForm because their operations are same

class EditPicture(View):

    def get(self,request,picture_id,*args,**kwargs):
        picture = None
        try:
            picture_id = UUID(picture_id)
            picture = ClinicPicture.objects.get(pk=picture_id)
        except:
            return redirect("/404")
        
        return render(request,"edit-picture/edit-picture.html",{
            "section":"مدیریت عکس ها",
            "page":"ویرایش عکس",
            "icon":"fa fa-pencil-square",
            "form":AddPictureForm(initial={"picture_title":picture.picture_title}),
            "picture":picture
        })

    def post(self,request,picture_id,*args,**kwargs):
        picture = None
        try:
            picture_id = UUID(picture_id)
            picture = ClinicPicture.objects.get(pk=picture_id)
        except:
            return redirect("/404")
        form = AddPictureForm(request.POST,request.FILES)
        edit_picture_permission_code = 32
        if not request.user.has_permission(edit_picture_permission_code):
            return redirect("/404")
        if form.is_valid():
            cd = form.cleaned_data
            picture.picture_title = cd['picture_title']
            picture.picture = cd['picture']
            picture.save()
            messages.success(request,"عکس مورد نظر با موفقیت ویرایش شد","success")
            return redirect("administration:picture-management")
        return render(request,"edit-picture/edit-picture.html",{
            "section":"مدیریت عکس ها",
            "page":"ویرایش عکس",
            "icon":"fa fa-pencil-square",
            "form":form,
            "picture":picture
        })