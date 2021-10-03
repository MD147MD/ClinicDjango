from django.shortcuts import render,redirect
from django.views import View
from siteSettings.models import SiteSettings
from accounts.models import User,Category,SubCategory,UserLoginAttempt
from django.db.models import Q
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
from .forms import LoginForm,VerifyPhoneForm
from random import randint


class Home(View):

    def get(self,request,*args,**kwargs):
        return render(request,'home/home.html')
    

class Login(View):
    
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/404')
        return render(request,'login/login.html',{"form":LoginForm()})
    
    def post(self,request,*args,**kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            # TODO : SEND SMS TO USER
            phone_number = form.cleaned_data["phone_number"]
            user = User.objects.filter(phone_number=phone_number).first()
            if not user:
                user = User.objects.create(phone_number=phone_number)
            UserLoginAttempt.objects.create(user=user,code=randint(100000,999999),ip=get_client_ip(request))
            messages.success(request,"کد راستی آزمایی برای شما ارسال شد","warning")
            request.session["phone_number"] = phone_number
            return redirect("core:verify-phone")
        return render(request,'login/login.html',{"form":form})


class VerifyPhone(View):

    def get(self,request,*args,**kwargs):
        phone_number = request.session.get("phone_number")
        if request.user.is_authenticated or not phone_number:
            return redirect('/404')
        return render(request,'verify-phone/verify-phone.html',{"form":VerifyPhoneForm()})

    def post(self,request,*args,**kwargs):
        form = VerifyPhoneForm(request.POST)
        phone_number = request.session.get("phone_number")
        if request.user.is_authenticated or not phone_number:
            return redirect('/404')
        if form.is_valid():
            user_attempt = UserLoginAttempt.objects.filter(user__phone_number=phone_number,code=int(form.cleaned_data["code"]),used=False).first()
            if user_attempt:
                user_attempt.used = True
                user_attempt.save()
                user = user_attempt.user
                if user.is_blocked or not user:
                    request.session.pop("phone_number")
                    messages.error(request,"شما توسط ادمین های سایت بلاک شده اید","danger")
                    return render(request,'verify-phone/verify-phone.html',{"form":form})
                login(request,user)
                request.session.pop("phone_number")
                messages.success(request,"شما با موفقیت وارد حساب کاربری خود شدید","success")
                return redirect("core:home")
            messages.error(request,"کد وارد شده نا معتبر است","danger")
        return render(request,'verify-phone/verify-phone.html',{"form":form})

class Logout(View):
    
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request,"شما با موفقیت از حساب کاربری خود خارج شدید","info")
            return redirect("core:home")
        return redirect("/404")



class Doctors(View):

    def get(self,request,*args,**kwargs):
        sub_categories_params = request.GET.getlist("sub-categories")
        sub_categories = SubCategory.objects.filter(id__in=sub_categories_params)
        doctors = []
        doctor_permission_code = 50
        if sub_categories:
            doctors = User.objects.filter(roles__permissions__permission_code=doctor_permission_code,categories__in=sub_categories)
        else:
            doctors = User.objects.filter(roles__permissions__permission_code=doctor_permission_code)
        return render(request,'doctors/doctors.html',{"doctors":doctors,"categories":Category.objects.all(),"selected_sub_categories":sub_categories})


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


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
