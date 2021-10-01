from django import forms



class AddPictureForm(forms.Form):
    picture_title = forms.CharField(max_length=80,min_length=2,error_messages={
        'min_length':'تعداد حروف موضوع عکس کمتر از حد مجاز است',
        'max_length':'تعداد حروف موضوع عکس بیشتر از حد مجاز است',
        'required':'لطفا موضوع عکس را وارد کنید'
    },widget=forms.TextInput({"placeholder":"موضوع عکس","class":"form-control"}))
    picture = forms.ImageField(required=True,error_messages={'invalid':'لطفا بجز عکس چیز دیگری انتخاب نکنید','required':'لطفا عکسی را انتخاب کنید'},widget=forms.FileInput(attrs={'style':'display:none','id':'picture'}))
