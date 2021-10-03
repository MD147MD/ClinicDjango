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