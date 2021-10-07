from django.views import View
from accounts.models import UserAppointment
from uuid import UUID
from django.contrib import messages
from django.shortcuts import redirect


class EditDoctorAppointment(View):

    def get(self,request,appointment_id,*args,**kwargs):
        edit_doctor_appointment_permission_code = 17
        if not request.user.has_permission(edit_doctor_appointment_permission_code):
            return redirect("/404")
        user_appointment = None
        try:
            UUID(appointment_id)
            user_appointment = UserAppointment.objects.get(id=appointment_id)
        except:
            return redirect("/404")
        user_appointment.used = not user_appointment.used
        user_appointment.save()
        messages.success(request,"نوبت مورد نظر با موفقیت ویرایش شد","info")
        return redirect("administration:doctor-appointments",user_appointment.doctor.id)