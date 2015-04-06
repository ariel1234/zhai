from django.db import models

import datetime
from django.utils import timezone

# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def was_created_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=30) <= self.created <= now