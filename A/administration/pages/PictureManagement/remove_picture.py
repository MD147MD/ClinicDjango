from django.shortcuts import redirect
from django.views import View
from pictures.models import ClinicPicture
from uuid import UUID
from django.contrib import messages


class RemovePicture(View):

    def get(self,request, picture_id,*args,**kwargs):
        picture = None
        try:
            picture_id = UUID(picture_id)
            picture = ClinicPicture.objects.get(pk=picture_id)
        except:
            return redirect("/404")
        remove_picture_permission_code = 33
        if not request.user.has_permission(remove_picture_permission_code):
            return redirect("/404")
        picture.is_removed = True
        picture.save()
        messages.success(request,"عکس مورد نظر با موفقیت حذف شد","success")
        return redirect("administration:picture-management")