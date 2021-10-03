from django import forms
from ckeditor.widgets import CKEditorWidget

class SiteSettingsForm(forms.Form):
    contact_us = forms.CharField(required=True,min_length=10,max_length=2000,error_messages={
        'required':'لطفا متن ارتباط با ما را وارد نمایید',
        'min_length':'تعداد حروف متن ارتباط با ما کمتر از حد مجاز است',
        'max_length':'تعداد حروف متن ارتباط با ما بیشتر از حد مجاز است'
    },widget=CKEditorWidget)
    about_us = forms.CharField(required=True,min_length=10,max_length=2000,error_messages={
        'required':'لطفا متن درباره ما را وارد نمایید',
        'min_length':'تعداد حروف متن درباره ما کمتر از حد مجاز است',
        'max_length':'تعداد حروف متن درباره ما بیشتر از حد مجاز است'
    },widget=CKEditorWidget)