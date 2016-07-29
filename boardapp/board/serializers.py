from rest_framework import serializers
from models import Board
from comment.serializers import CommentListSerializer


class BoardListSerializer(serializers.ModelSerializer):
    writer = serializers.CharField(source="member.user", read_only=True)
    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ("id", "title", "content", "view_cnt", "regdt", "member",  "writer", "comments")

