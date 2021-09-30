from django.db import models
import uuid
from .managers import MainManager


class ClinicPicture(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    picture_title = models.CharField(max_length=100)
    picture = models.ImageField(null=True,blank=True)
    objects = MainManager()
    is_removed = models.BooleanField(default=False)
    craeted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.picture_title