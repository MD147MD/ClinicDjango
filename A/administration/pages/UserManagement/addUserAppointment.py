from django.shortcuts import render,redirect
from django.views import View
from accounts.models import User,UserAppointment
from uuid import UUID
from administration.forms import AddUserAppointmentForm
from django.contrib import messages


class AddUserAppointment(View):

    def get(self,request,user_id,*args,**kwargs):
        user = None
        try:
            user_id = UUID(user_id)
            user = User.objects.get(pk=user_id)
        except:
            return redirect("/404")

        return render(request,"add-user-appointment/add-user-appointment.html",
        {
            "section":"مدیریت کاربران",
            "page":"افزودن نوبت",
            "icon":"fa fa-plus",
            "form":AddUserAppointmentForm()
        })


    def post(self,request,user_id,*args,**kwargs):
        user = None
        try:
            user_id = UUID(user_id)
            user = User.objects.get(pk=user_id)
        except:
            return redirect("/404")
        add_user_appointment_permission_code = 16
        if not request.user.has_permission(add_user_appointment_permission_code):
            return redirect("/404")
        form = AddUserAppointmentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # doctor_id = cd["selected_doctor"]
            # doctor = User.objects.filter(id=doctor_id).first()
            # if not doctor:
            #     return redirect("/404")
            UserAppointment.objects.create(user=user,doctor=cd['selected_doctor'])
            messages.success(request,"نوبت جدید با موفقیت اضافه شد","success")
            return redirect("administration:user-appointments",user.id)
        return render(request,"add-user-appointment/add-user-appointment.html",
        {
            "section":"مدیریت کاربران",
            "page":"افزودن نوبت",
            "icon":"fa fa-plus",
            "form":form
        })
    
