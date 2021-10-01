from django.views import View
from django.http import HttpResponse

class UserActions(View):
    
    def get(self,request,user_id,*args,**kwargs):
        return HttpResponse("User Actions")