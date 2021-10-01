from django.shortcuts import render
from django.views import View
from accounts.models import Category
from django.core.paginator import Paginator


class CategoryManagement(View):

    def get(self,request):

        search = request.GET.get("search").strip() if request.GET.get("search") else ""
        page = request.GET.get("page") if request.GET.get("page") else 1

        try:
            page = int(page)
        except:
            page = 1

        categories = []

        if search:
            categories = Category.objects.filter(category_name__icontains=search)
        else:
            categories = Category.objects.all()
        
        category_pages = Paginator(categories, 10)
        page_count = category_pages.num_pages
        page = page if page <= page_count else 1
        paginated_categories = category_pages.page(page)
        max_page = page + 3 if (page + 3) <= page_count else page_count
        min_page = page - 3 if (page - 3) >= 1 else 1
        add_category_permission_code = 41
        edit_category_permission_code = 42
        remove_category_permission_code = 43
        return render(request,"category-management/category-management.html",{
            "section":"مدیریت دسته ها",
            "page":"دیدن دسته ها",
            "icon":"fa fa-th-large",
            "categories":paginated_categories.object_list,
            "page_count":page_count,
            "has_next":paginated_categories.has_next(),
            "has_previous":paginated_categories.has_previous(),
            "min_page":min_page,
            "max_page":max_page,
            "current_page":page,
            "search":search,
            "page_range":range(min_page,max_page + 1),
            "can_add_category":request.user.has_permission(add_category_permission_code),
            "can_edit_category":request.user.has_permission(edit_category_permission_code),
            "can_remove_category":request.user.has_permission(remove_category_permission_code)
        })