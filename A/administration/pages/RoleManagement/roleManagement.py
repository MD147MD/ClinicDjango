from django.shortcuts import render
from django.views import View
from accounts.models import Role
from django.core.paginator import Paginator


class RoleManagement(View):

    def get(self,request):

        search = request.GET.get("search").strip() if request.GET.get("search") else ""
        page = request.GET.get("page") if request.GET.get("page") else 1

        try:
            page = int(page)
        except:
            page = 1

        roles = []

        if search:
            roles = Role.objects.filter(role_name__icontains=search).order_by("-id")
        else:
            roles = Role.objects.all().order_by("-id")
        
        role_pages = Paginator(roles, 10)
        page_count = role_pages.num_pages
        page = page if page <= page_count else 1
        paginated_roles = role_pages.page(page)
        max_page = page + 3 if (page + 3) <= page_count else page_count
        min_page = page - 3 if (page - 3) >= 1 else 1
        add_role_permission_code = 21
        edit_role_permission_code = 22
        remove_role_permission_code = 23
        return render(request,"role-management/role-management.html",{
            "section":"مدیریت نقش ها",
            "page":"دیدن نقش ها",
            "icon":"fa fa-tags",
            "roles":paginated_roles.object_list,
            "page_count":page_count,
            "has_next":paginated_roles.has_next(),
            "has_previous":paginated_roles.has_previous(),
            "min_page":min_page,
            "max_page":max_page,
            "current_page":page,
            "search":search,
            "page_range":range(min_page,max_page + 1),
            "can_add_role":request.user.has_permission(add_role_permission_code),
            "can_edit_role":request.user.has_permission(edit_role_permission_code),
            "can_remove_role": request.user.has_permission(remove_role_permission_code)
        })