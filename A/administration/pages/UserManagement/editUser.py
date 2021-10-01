from django.shortcuts import render,redirect
from django.views import View
from accounts.models import User
from administration.forms import EditUserForm
from uuid import UUID
from django.contrib import messages

class EditUser(View):

    def get(self,request,user_id,*args,**kwargs):
        try:
            UUID(user_id)
        except:
            return redirect("/administration/user-management")
        user = User.objects.filter(pk=user_id).first()
        if not user:
            return redirect("/administration/user-management")
        data = {
            'name':user.name,
            'family':user.family,
            'phone_number':user.phone_number,
            'email':user.email,
            'age':user.age,
            'doctor_shift':user.doctor_shift,
            'doctor_resume':user.doctor_resume,
            'roles':list(user.roles.values_list('id',flat=True)),
            'categories':list(user.categories.values_list('id',flat=True))
        }
        doctor_permission_code = 50
        return render(request,"edit-user/edit-user.html",{
            "section":"مدیریت کاربران",
            "page":"ویرایش کاربر",
            "icon":"fa fa-pencil",
            "form":EditUserForm(initial=data),
            "user":user,
            "is_doctor":user.has_permission(doctor_permission_code)
        })

    def post(self,request,user_id,*args,**kwargs):    
        try:
            UUID(user_id)
        except:
            return redirect("/administration/user-management")
        user = User.objects.filter(pk=user_id).first()
        edit_user_permission_code = 12
        if not user or not request.user.has_permission(edit_user_permission_code):
            return redirect("/404")
        form = EditUserForm(request.POST,request.FILES)
        doctor_permission_code = 50
        if form.is_valid():
            cd = form.cleaned_data
            if user.phone_number != cd['phone_number'] and User.objects.filter(phone_number=cd['phone_number']).first():
                form.add_error('phone_number','کاربری با شماره تلفن وارد شده از قبل وجود دارد')
                return render(request,"edit-user/edit-user.html",{
                    "section":"مدیریت کاربران",
                    "page":"ویرایش کاربر",
                    "icon":"fa fa-pencil",
                    "form":form,
                    "user":user,
                    "is_doctor":user.has_permission(doctor_permission_code)
                })
            user.name = cd['name']
            user.family = cd['family']
            user.phone_number = cd['phone_number']
            user.email = cd['email']
            user.age = cd['age']
            user.profile_img = cd['profile_img'] if cd['profile_img'] else user.profile_img
            user.doctor_shift = cd['doctor_shift']
            user.doctor_resume = cd['doctor_resume']
            user.roles.set(cd['roles'])
            user.categories.set(cd['categories'])
            user.save()
            messages.success(request,"کاربر مورد نظر با موفقیت ویرایش شد","info")
            return redirect("/administration/user-management")
        return render(request,"edit-user/edit-user.html",{
            "section":"مدیریت کاربران",
            "page":"ویرایش کاربر",
            "icon":"fa fa-pencil",
            "form":form,
            "user":user,
            "is_doctor":user.has_permission(doctor_permission_code)
        })


