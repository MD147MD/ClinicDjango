from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from .forms import UserChangeForm,UserCreationForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('phone_number', 'is_active', 'is_removed')
    list_filter = ('is_admin','is_active','is_removed')

    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ('name','family','email','age','doctor_shift','doctor_resume','profile_img','categories')}),
        ('Other', {'fields': ('is_admin','is_blocked','is_removed','is_active','roles')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('phone_number', 'password'),
        }),
    )
    search_fields = ('phone_number',)
    ordering = ('phone_number',)
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Role)
admin.site.register(Category)
admin.site.register(Permission)
admin.site.register(SubCategory)
admin.site.register(UserAppointment)
admin.site.register(UserLoginAttempt)