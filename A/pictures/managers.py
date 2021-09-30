from django.db import models


class MainManager(models.Manager):

   def get_queryset(self):
        return super().get_queryset().filter(is_removed=False)
