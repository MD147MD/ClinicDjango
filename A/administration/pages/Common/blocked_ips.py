


from django.shortcuts import render
from django.views import View
from accounts.models import BlockedIp
from django.core.paginator import Paginator


class IpManagement(View):

    def get(self,request):

        search = request.GET.get("search").strip() if request.GET.get("search") else ""
        page = request.GET.get("page") if request.GET.get("page") else 1

        try:
            page = int(page)
        except:
            page = 1

        ips = []

        if search:
            ips = BlockedIp.objects.filter(ip__icontains=search).order_by("-created_at")
        else:
            ips = BlockedIp.objects.all().order_by("-created_at")
        
        ip_pages = Paginator(ips, 10)
        page_count = ip_pages.num_pages
        page = page if page <= page_count else 1
        paginated_ips = ip_pages.page(page)
        max_page = page + 3 if (page + 3) <= page_count else page_count
        min_page = page - 3 if (page - 3) >= 1 else 1
        add_ip_permission_code = 81
        remove_ip_permission_code = 83
        return render(request,"blocked-ips/blocked-ips.html",{
            "section":"عمومی",
            "page":"آیپی های بلاک شده",
            "icon":"fa fa-ban",
            "ips":paginated_ips.object_list,
            "page_count":page_count,
            "has_next":paginated_ips.has_next(),
            "has_previous":paginated_ips.has_previous(),
            "min_page":min_page,
            "max_page":max_page,
            "current_page":page,
            "search":search,
            "page_range":range(min_page,max_page + 1),
            "can_add_ip":request.user.has_permission(add_ip_permission_code),
            "can_remove_ip": request.user.has_permission(remove_ip_permission_code)
        })