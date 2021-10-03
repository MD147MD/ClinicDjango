from django.shortcuts import render,redirect
from django.views import View
from siteSettings.models import SiteSettings
from accounts.models import User,Category


class Home(View):

    def get(self,request,*args,**kwargs):
        return render(request,'home/home.html')
    

class Login(View):
    
    def get(self,request,*args,**kwargs):
        return render(request,'login/login.html')


class Logout(View):
    
    def get(self,request,*args,**kwargs):
        pass


class Doctors(View):

    def get(self,request,*args,**kwargs):
        doctor_permission_code = 50
        doctors = User.objects.filter(roles__permissions__permission_code=doctor_permission_code)
        return render(request,'doctors/doctors.html',{"doctors":doctors,"categories":Category.objects.all()})


class UserPanel(View):
    
    def get(self,request,*args,**kwargs):
        return render(request,'user-panel/user-panel.html')


class Pictures(View):

    def get(self,request,*args,**kwargs):
        return render(request,'pictures/pictures.html')
    

class ContactUs(View):

    def get(self,request,*args,**kwargs):
        settings = SiteSettings.objects.first()
        if settings:
            return render(request,'contact-us/contact-us.html',{"settings":settings})
        return redirect("/404")


class AboutUs(View):

    def get(self,request,*args,**kwargs):
        settings = SiteSettings.objects.first()
        if settings:
            return render(request,'about-us/about-us.html',{"settings":settings})
        return redirect("/404")


