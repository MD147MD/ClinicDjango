from django.views import View
from django.shortcuts import redirect,render
from accounts.models import User,UserAppointment

from django.db.models import Q
from django.core.paginator import Paginator

class UserAppointments(View):

    def get(self,request,user_id,*args,**kwargs):
        user = User.objects.filter(id=user_id).first()
        if not user:
            return redirect("/404")
        search = request.GET.get("search").strip() if request.GET.get("search") else ""
        page = request.GET.get("page") if request.GET.get("page") else 1

        try:
            page = int(page)
        except:
            page = 1

        appointments = []

        if search:
            appointments = user.user_appointments.filter(Q(doctor__name__icontains=search) | Q(doctor__family__icontains=search) | Q(doctor__phone_number__icontains=search)).order_by("-id")
        else:
            appointments = user.user_appointments.all().order_by("-id")
        
        appointment_pages = Paginator(appointments, 10)
        page_count = appointment_pages.num_pages
        page = page if page <= page_count else 1
        paginated_appointments = appointment_pages.page(page)
        max_page = page + 3 if (page + 3) <= page_count else page_count
        min_page = page - 3 if (page - 3) >= 1 else 1
        add_appointment_permission_code = 16
        edit_appointment_permission_code = 17
        return render(request,"user-appointment-management/user-appointment-management.html",{
            "section":"مدیریت نوبت ها",
            "page":"دیدن نوبت ها",
            "icon":"fa fa-id-card",
            "appointments":paginated_appointments.object_list,
            "page_count":page_count,
            "has_next":paginated_appointments.has_next(),
            "has_previous":paginated_appointments.has_previous(),
            "min_page":min_page,
            "max_page":max_page,
            "current_page":page,
            "search":search,
            "page_range":range(min_page,max_page + 1),
            "can_add_appointment":request.user.has_permission(add_appointment_permission_code),
            "can_edit_appointment":request.user.has_permission(edit_appointment_permission_code),
        })