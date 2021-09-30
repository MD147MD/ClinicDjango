from django.shortcuts import render
from django.views import View
from accounts.models import User


class Index(View):

    def get(self,request,*args,**kwargs):
        return render(request,"index/index.html",{
            "section":"خانه",
            "page":"داشبرد",
            "icon":"fa fa-home",
            "user_count":User.objects.count()
        })