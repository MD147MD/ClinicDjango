from django.views import View
from django.shortcuts import render


class SmsLogs(View):
    
    def get(self,request,*args,**kwargs):
        return render(request,"sms-logs/sms-logs.html")