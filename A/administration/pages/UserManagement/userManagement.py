from django.shortcuts import render
from django.views import View
from accounts.models import User
from django.db.models import Q
from django.core.paginator import Paginator


class UserManagement(View):

    def get(self,request):

        search = request.GET.get("search").strip() if request.GET.get("search") else ""
        page = request.GET.get("page") if request.GET.get("page") else 1

        try:
            page = int(page)
        except:
            page = 1

        users = []

        if search:
            users = User.objects.filter(Q(phone_number__icontains=search) | Q(name__icontains=search) | Q(family__icontains=search))
        else:
            users = User.objects.all()
        
        user_pages = Paginator(users, 10)
        page_count = user_pages.num_pages
        page = page if page <= page_count else 1
        paginated_users = user_pages.page(page)
        max_page = page + 3 if (page + 3) <= page_count else page_count
        min_page = page - 3 if (page - 3) >= 1 else 1
        return render(request,"user-management/user-management.html",{
            "section":"مدیریت کاربران",
            "page":"دیدن کاربران",
            "icon":"fa fa-users",
            "users":paginated_users.object_list,
            "page_count":page_count,
            "has_next":paginated_users.has_next(),
            "has_previous":paginated_users.has_previous(),
            "min_page":min_page,
            "max_page":max_page,
            "current_page":page,
            "search":search,
            "page_range":range(min_page,max_page + 1),
        })