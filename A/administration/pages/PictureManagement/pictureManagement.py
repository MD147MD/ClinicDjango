from django.shortcuts import render
from django.views import View
from pictures.models import ClinicPicture
from django.core.paginator import Paginator


class PictureManagement(View):

    def get(self,request):

        search = request.GET.get("search").strip() if request.GET.get("search") else ""
        page = request.GET.get("page") if request.GET.get("page") else 1

        try:
            page = int(page)
        except:
            page = 1

        pictures = []

        if search:
            pictures = ClinicPicture.objects.filter(picture_title__icontains=search)
        else:
            pictures = ClinicPicture.objects.all()
        
        picture_pages = Paginator(pictures, 10)
        page_count = picture_pages.num_pages
        page = page if page <= page_count else 1
        paginated_pictures = picture_pages.page(page)
        max_page = page + 3 if (page + 3) <= page_count else page_count
        min_page = page - 3 if (page - 3) >= 1 else 1
        add_picture_permission_code = 31
        edit_picture_permission_code = 32
        remove_picture_permission_code = 33
        return render(request,"picture-management/picture-management.html",{
            "section":"مدیریت عکس ها",
            "page":"دیدن عکس ها",
            "icon":"fa fa-files-o",
            "pictures":paginated_pictures.object_list,
            "page_count":page_count,
            "has_next":paginated_pictures.has_next(),
            "has_previous":paginated_pictures.has_previous(),
            "min_page":min_page,
            "max_page":max_page,
            "current_page":page,
            "search":search,
            "page_range":range(min_page,max_page + 1),
            "can_add_picture":request.user.has_permission(add_picture_permission_code),
            "can_edit_picture":request.user.has_permission(edit_picture_permission_code),
            "can_remove_picture":request.user.has_permission(remove_picture_permission_code)
        })