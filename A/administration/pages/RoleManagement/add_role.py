from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class AddRole(View):

    def get(self,request):
        return HttpResponse("Add Role")