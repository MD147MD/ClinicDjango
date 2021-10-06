from django import forms



class LoginForm(forms.Form):
    phone_number = forms.CharField(label="",max_length=11,min_length=11,required=True,error_messages={
        "min_length":"تعداد حروف شماره تلفن کمتر از حد مجاز است",
        "max_length":"تعداد حروف شماره تلفن بیشتر از حد مجاز است",
        "required":"لطفا شماره تلفن را وارد نمایید",
        "invalid":"لطفا بجز عدد چیز دیگری وارد نکنید"
    },widget=forms.TextInput(attrs={"class":"animate__animated animate__fadeInLeftBig","placeholder":"شماره تلفن","id":"phone-number"}))

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        try:
            int(phone_number)
        except:
            raise forms.ValidationError("شماره تلفن وارد شده معتبر نیست")
        if not phone_number.startswith("09"):
            raise forms.ValidationError("شماره تلفن وارد شده معتبر نیست")
        return phone_number


class VerifyPhoneForm(forms.Form):
    code = forms.CharField(label="",required=True,error_messages={
        "required":"لطفا کد را وارد نمایید",
        "invalid":"لطفا بجز عدد چیز دیگری وارد نکنید"
    },widget=forms.TextInput(attrs={"class":"animate__animated animate__fadeInLeftBig","placeholder":"کد راستی آزمایی","id":"phone-number"}))

    def clean_code(self):
        code = self.cleaned_data["code"]
        try:
            int(code)
        except:
            raise forms.ValidationError("کد وارد شده معتبر نیست")
        return code


class EditUserForm(forms.Form):
    name = forms.CharField(label="",required=False,max_length=70,min_length=3,error_messages={
        "min_length":"تعداد حروف نام کمتر از حد مجاز است",
        "max_length":"تعداد حروف نام بیشتر از حد مجاز است"
    },widget=forms.TextInput(attrs={"placeholder":"نام"}))

    family = forms.CharField(label="",required=False,max_length=70,min_length=3,error_messages={
        "min_length":"تعداد حروف نام خانوادگی کمتر از حد مجاز است",
        "max_length":"تعداد حروف نام خانوادگی بیشتر از حد مجاز است"
    },widget=forms.TextInput(attrs={"placeholder":"نام خانوادگی"}))

    age = forms.IntegerField(max_value=120
        ,min_value=4,
        required=False,
        error_messages={'max_value':'سن وارد شده بیشتر از حد مجاز است',
        'min_value':'سن وارد شده کمتر از حد مجاز است','invalid':'سن وارد شده معتبر نیست'}
        ,widget=forms.NumberInput({'placeholder':'سن'}))


    email = forms.CharField(label="",required=False,max_length=70,min_length=10,error_messages={
        "min_length":"تعداد حروف ایمیل کمتر از حد مجاز است",
        "max_length":"تعداد حروف ایمیل بیشتر از حد مجاز است"
    },widget=forms.EmailInput(attrs={"placeholder":"ایمیل"}))

    profile_img = forms.ImageField(label="",required=False,error_messages={'invalid':'لطفا بجز عکس چیز دیگری انتخاب نکنید'},widget=forms.FileInput(attrs={'style':'display:none','id':'profile_img'}))

    doctor_visit_cost = forms.IntegerField(required=False,label="",max_value=10000000,min_value=10000,error_messages={
            "min_value":"مقدار قیمت ویزیت از حد مجاز کمتر است",
            "max_value":"مقدار قیمت ویزیت از حد مجاز بیشتر است"
        },widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"قیمت ویزیت (به تومان)"}))


    doctor_shift = forms.CharField(label="",required=False,max_length=200
    ,min_length=10,
    error_messages={'max_length':'تعداد حروف شیفت دکتر بیشتر از حد مجاز است',
    'min_length':'تعداد حروف شیفت دکتر کمتر از حد مجاز است'}
    ,widget=forms.Textarea({'placeholder':'شیفت دکتر','rows':2,"class":"form-control"}))

    doctor_resume = forms.CharField(label="",required=False,max_length=700
    ,min_length=10,
    error_messages={'max_length':'تعداد حروف رزومه دکتر بیشتر از حد مجاز است',
    'min_length':'تعداد حروف رزومه دکتر کمتر از حد مجاز است'}
    ,widget=forms.Textarea({'placeholder':'رزومه دکتر','rows':5,"class":"form-control"}))
