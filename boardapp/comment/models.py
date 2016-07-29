from __future__ import unicode_literals

from django.db import models
from member.models import Member
from board.models import Board

class Comment(models.Model):
    comment = models.TextField()
    board = models.ForeignKey(Board, null=True, related_name="comments")
    member = models.ForeignKey(Member, null=True, related_name="comment_writer")
    regdt = models.DateTimeField(null=True, auto_now_add=True)

    class Meta():
        db_table = "tbl_comment"
