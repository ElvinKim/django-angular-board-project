from __future__ import unicode_literals

from django.db import models
from member.models import Member

class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    member = models.ForeignKey(Member, null=True)
    view_cnt = models.IntegerField(default=0)
    moddt = models.DateTimeField()
    regdt = models.DateTimeField()

    class Meta():
        db_table = "tbl_board"
