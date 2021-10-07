from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import *
import uuid
import datetime
from django.utils import timezone


class Permission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    permission_name = models.CharField(max_length=120)
    permission_code = models.PositiveSmallIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.permission_name


class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role_name = models.CharField(max_length=120)
    permissions = models.ManyToManyField(Permission,null=True,blank=True)
    is_removed = models.BooleanField(default=False)
    objects = MainManager()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role_name

# This model built for doctor category (filters in front end)
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=120)
    is_removed = models.BooleanField(default=False)
    objects = MainManager()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent_category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='sub_categories')
    sub_category_name = models.CharField(max_length=120)
    is_removed = models.BooleanField(default=False)
    objects = MainManager()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sub_category_name


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=10,blank=True,null=True)
    name = models.CharField(max_length=120,null=True,blank=True)
    family = models.CharField(max_length=120,null=True,blank=True)
    email = models.CharField(max_length=120,null=True,blank=True)
    phone_number = models.CharField(max_length=40,unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)
    objects = UserManager()
    age = models.PositiveSmallIntegerField(null=True,blank=True)
    profile_img = models.ImageField(null=True,blank=True)
    doctor_visit_cost = models.PositiveIntegerField(null=True,blank=True)
    doctor_shift = models.CharField(max_length=120,null=True,blank=True)
    doctor_resume = models.TextField(max_length=3000,null=True,blank=True)
    categories = models.ManyToManyField(SubCategory,null=True,blank=True,related_name="users")
    roles = models.ManyToManyField(Role,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return self.phone_number

    def has_permission(self,permission_code):
        user_roles = self.roles.all()
        permission = None
        for role in user_roles:
            permission = role.permissions.filter(permission_code=permission_code).first()
            if permission:
                break
        return True if permission else False

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_doctor(self):
        doctor_permission_code = 50
        return self.has_permission(doctor_permission_code)
        
def get_till():
        return timezone.now() + datetime.timedelta(minutes=15)


class UserLoginAttempt(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='login_attempts')
    code = models.PositiveIntegerField()
    ip = models.CharField(max_length=120,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    till = models.DateTimeField(default=get_till)
    used = models.BooleanField(default=False)
 
    def __str__(self):
        return self.user.phone_number


class UserAppointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='doctor_appointments',null=True,blank=True)
    user = models.ForeignKey('User',on_delete=models.CASCADE,related_name='user_appointments',null=True,blank=True)
    used = models.BooleanField(default=False)
    paid_cost = models.PositiveIntegerField(null=True,blank=True)
    is_paid = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)
    objects = MainManager()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.phone_number


class BlockedIp(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ip = models.CharField(max_length=120)
    is_removed = models.BooleanField(default=False)
    objects = MainManager()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.ip