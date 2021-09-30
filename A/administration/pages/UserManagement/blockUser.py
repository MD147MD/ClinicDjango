from django.views import View
from django.shortcuts import redirect
from uuid import UUID
from accounts.models import User
from django.contrib import messages


class BlockUser(View):

    def get(self,request,*args,**kwargs):
        try:
            user_id = kwargs.get("user_id")
            user_id = UUID(user_id)
            user = User.objects.filter(pk=user_id)[0]
            if user:
                user.is_blocked = not user.is_blocked
                user.save()
                message_result = "بلاک" if user.is_blocked else "آن بلاک"
                messages.success(request,f"کاربر مورد نظر با موفقیت {message_result} شد","success")
        except:
            pass    
        return redirect("/administration/user-management")