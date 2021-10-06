from django.shortcuts import render
from django.views import View
from accounts.models import User,UserAppointment,UserLoginAttempt


class Index(View):

    def get(self,request,*args,**kwargs):
        doctor_permission_code = 50
        return render(request,"index/index.html",{
            "section":"خانه",
            "page":"داشبرد",
            "icon":"fa fa-home",
            "user_count":User.objects.count(),
            "appointment_count":UserAppointment.objects.count(),
            "sms_count":UserLoginAttempt.objects.count(),
            "doctors_count":User.objects.filter(roles__permissions__permission_code=doctor_permission_code).count()
        })