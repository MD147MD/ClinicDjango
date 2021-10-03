from django.db import models
from accounts.models import User
from pictures.models import ClinicPicture
import uuid

class SiteSettings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    about_us_text = models.CharField(max_length=1000)
    contact_us_text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'SiteSettings'