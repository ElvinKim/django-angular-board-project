from __future__ import unicode_literals

from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.IntegerField(default=0)
    view_cnt = models.IntegerField(default=0)
    moddt = models.DateTimeField()
    regdt = models.DateTimeField()

    class Meta():
        db_table = "tbl_board"
