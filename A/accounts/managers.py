from .models import *
from django.contrib.auth.models import BaseUserManager
from django.db import models
from uuid import uuid4

class UserManager(BaseUserManager):
    
    def create_user(self, phone_number,email=None):     
        if not phone_number:
            raise ValueError('Users must have a Phone Number')
            
        user = self.model(
            phone_number=phone_number 
        )
        user.set_password(uuid4())
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number,email=None):
        user = self.create_user(
            phone_number=phone_number,
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user

    def get_queryset(self):
        return super().get_queryset().filter(is_removed=False)


class MainManager(models.Manager):

   def get_queryset(self):
        return super().get_queryset().filter(is_removed=False)
