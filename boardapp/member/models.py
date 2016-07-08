from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    moddt = models.DateTimeField()
    regdt = models.DateTimeField()

    class Meta():
        db_table = "tbl_member"
