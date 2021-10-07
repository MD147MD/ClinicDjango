from django.views import View
from django.shortcuts import redirect,render
from accounts.models import User,UserAppointment
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models import Sum


class DoctorAppointments(View):

    def get(self,request,user_id,*args,**kwargs):
        doctor = User.objects.filter(id=user_id).first()
        if not doctor or not doctor.is_doctor:
            return redirect("/404")

        appointments = UserAppointment.objects.filter(doctor=doctor)
        total = appointments.filter(is_paid=True).aggregate(total=Sum('paid_cost'))['total']
        edit_appointment_permission_code = 17
        return render(request,"doctor-appointments/doctor-appointments.html",{
            "section":"مدیریت نوبت ها",
            "page":"دیدن نوبت ها",
            "icon":"fa fa-id-card",
            "appointments":appointments,
            "can_edit_appointment":request.user.has_permission(edit_appointment_permission_code),
            "sum":total
        })