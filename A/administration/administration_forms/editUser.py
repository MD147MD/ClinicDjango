from django import forms
from accounts.models import Role,SubCategory
from uuid import uuid4
import os


class EditUserForm(forms.Form):
    
    name = forms.CharField(max_length=30
    ,min_length=3,
    required=False,
    error_messages={'max_length':'تعداد حروف نام بیشتر از حد مجاز است',
    'min_length':'تعداد حروف نام کمتر از حد مجاز است'}
    ,widget=forms.TextInput({'placeholder':'نام','class':'form-control'}))

    family = forms.CharField(max_length=30
    ,min_length=3,
    required=False,
    error_messages={'max_length':'تعداد حروف نام خانوادگی بیشتر از حد مجاز است',
    'min_length':'تعداد حروف نام خانوادگی کمتر از حد مجاز است'}
    ,widget=forms.TextInput({'placeholder':'نام خانوادگی','class':'form-control'}))

    phone_number = forms.CharField(max_length=11,min_length=11,required=True,
    error_messages={'max_length':'تعداد حروف شماره تلفن بیشتر از حد مجاز است'
    ,'min_length':'تعداد حروف شماره تلفن کمتر از حد مجاز است','required':'لطفا شماره تلفن را وارد کنید'},widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'09xxxxxxxxx'}))

    email = forms.EmailField(max_length=70
    ,min_length=10,
    required=False,
    error_messages={'max_length':'تعداد حروف ایمیل بیشتر از حد مجاز است',
    'min_length':'تعداد حروف ایمیل کمتر از حد مجاز است','invalid':'لطفا یک ایمیل معتبر وارد نمایید'}
    ,widget=forms.EmailInput({'placeholder':'ایمیل','class':'form-control'}))

    age = forms.IntegerField(max_value=120
    ,min_value=4,
    required=False,
    error_messages={'max_value':'سن وارد شده بیشتر از حد مجاز است',
    'min_value':'سن وارد شده کمتر از حد مجاز است','invalid':'سن وارد شده معتبر نیست'}
    ,widget=forms.NumberInput({'placeholder':'00','class':'form-control'}))

    profile_img = forms.ImageField(required=False,error_messages={'invalid':'لطفا بجز عکس چیز دیگری انتخاب نکنید'},widget=forms.FileInput(attrs={'style':'display:none','id':'profile_img'}))
    try:
        # categories = forms.MultipleChoiceField(required=False,widget=forms.SelectMultiple(attrs={"class":"form-control"}),
        # choices=SubCategory.objects.all().values_list("id","sub_category_name"))
        categories = forms.ModelMultipleChoiceField(queryset=SubCategory.objects.all(),widget=forms.SelectMultiple(attrs={"class":"form-control"}))
    except:
        categories = None

    doctor_visit_cost = forms.IntegerField(required=False,label="",max_value=10000000,min_value=10000,error_messages={
        "min_value":"مقدار قیمت ویزیت از حد مجاز کمتر است",
        "max_value":"مقدار قیمت ویزیت از حد مجاز بیشتر است"
    },widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"قیمت ویزیت"}))

    doctor_shift = forms.CharField(max_length=200
    ,min_length=10,
    required=False,
    error_messages={'max_length':'تعداد حروف شیفت دکتر بیشتر از حد مجاز است',
    'min_length':'تعداد حروف شیفت دکتر کمتر از حد مجاز است'}
    ,widget=forms.Textarea({'placeholder':'شیفت دکتر','class':'form-control','rows':2}))

    doctor_resume = forms.CharField(max_length=700
    ,min_length=10,
    required=False,
    error_messages={'max_length':'تعداد حروف رزومه دکتر بیشتر از حد مجاز است',
    'min_length':'تعداد حروف رزومه دکتر کمتر از حد مجاز است'}
    ,widget=forms.Textarea({'placeholder':'رزومه دکتر','class':'form-control','rows':5}))
    try:
        # roles = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple(),choices=Role.objects.all().values_list('id','role_name'))
        roles = forms.ModelMultipleChoiceField(queryset=Role.objects.all(),widget=forms.CheckboxSelectMultiple())
    except:
        roles = None
        
    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        try:
            int(phone_number)
            if phone_number[0:2] != "09":
                raise forms.ValidationError("شماره تلفن وارد شده معتبر نیست")
        except:
            raise forms.ValidationError("شماره تلفن وارد شده معتبر نیست")
        return phone_number
    
   