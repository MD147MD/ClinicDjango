from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class EditSiteSettings(View):

    def get(self,request,*args,**kwargs):
        return HttpResponse("Edit SiteSettings")