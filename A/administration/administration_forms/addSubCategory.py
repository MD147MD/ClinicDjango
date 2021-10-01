from django import forms



class AddSubCategoryForm(forms.Form):
    sub_category_name = forms.CharField(max_length=80,min_length=2,error_messages={
        'min_length':'تعداد حروف نام زیر دسته کمتر از حد مجاز است',
        'max_length':'تعداد حروف نام زیر دسته بیشتر از حد مجاز است',
        'required':'لطفا نام دسته را وارد کنید'
    },widget=forms.TextInput({"placeholder":"نام زیر دسته","class":"form-control"}))
    