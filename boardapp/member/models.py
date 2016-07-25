from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class Member(models.Model):
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=64)
    moddt = models.DateTimeField(default=datetime.now, blank=True)
    regdt = models.DateTimeField(default=datetime.now, blank=True)

    class Meta():
        db_table = "tbl_member"
