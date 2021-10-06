from django import forms
from accounts.models import Permission



class AddRoleForm(forms.Form):
    role_name = forms.CharField(max_length=80,min_length=2,error_messages={
        'min_length':'تعداد حروف نام نقش کمتر از حد مجاز است',
        'max_length':'تعداد حروف نام نقش بیشتر از حد مجاز است',
        'required':'لطفا نام نقش را وارد کنید'
    },widget=forms.TextInput({"placeholder":"نام نقش","class":"form-control"}))
    try:
        # permissions = forms.MultipleChoiceField(required=True,error_messages={"required":"لطفا حداقل یک دسترسی انتخاب کنید"},widget=forms.SelectMultiple(attrs={"class":"form-control"}),
        # choices=Permission.objects.all().values_list("id","permission_name"))
        permissions = forms.ModelMultipleChoiceField(queryset=Permission.objects.all(),required=True,error_messages={"required":"لطفا حداقل یک دسترسی انتخاب کنید"},widget=forms.SelectMultiple(attrs={"class":"form-control"}))
    except:
        permissions = None