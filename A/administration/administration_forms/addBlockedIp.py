from django import forms


class AddBlockedIpForm(forms.Form):
    ip = forms.CharField(label='',required=True,max_length=120,min_length=5,error_messages={
        'min_length':'تعداد حروف آدرس آیپی کمتر از حد مجاز است',
        'max_length':'تعداد حروف آدرس آیپی بیشتر از حد مجاز است',
        'required':'لطفا آدرس آیپی را وارد کنید'
    },widget=forms.TextInput(attrs={'placeholder':'آدرس آیپی','class':'form-control'}))