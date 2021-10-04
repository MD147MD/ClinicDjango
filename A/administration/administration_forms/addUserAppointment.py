from django import forms
from accounts.models import User


doctor_permission_code = 50

class AddUserAppointmentForm(forms.Form):
    selected_doctor = forms.ChoiceField(choices=User.objects.filter(roles__permissions__permission_code=doctor_permission_code).values_list("id","phone_number"),widget=forms.Select(attrs={"class":"form-control"}))
  
  