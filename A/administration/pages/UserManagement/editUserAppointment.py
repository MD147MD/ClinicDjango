from django.views import View
from accounts.models import UserAppointment
from uuid import UUID
from django.contrib import messages
from django.shortcuts import redirect


class EditUserAppointment(View):

    def get(self,request,appointment_id,*args,**kwargs):
        user_appointment = None
        try:
            UUID(appointment_id)
            user_appointment = UserAppointment.objects.get(id=appointment_id)
        except:
            redirect("/404")
        user_appointment.used = not user_appointment.used
        user_appointment.save()
        messages.success(request,"نوبت مورد نظر با موفقیت ویرایش شد","info")
        return redirect("administration:user-appointments",user_appointment.user.id)