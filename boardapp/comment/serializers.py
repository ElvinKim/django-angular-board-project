from rest_framework import serializers
from models import Comment

class CommentListSerializer(serializers.ModelSerializer):
    comment_writer = serializers.CharField(source="member.user", read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "comment", "board", "member", "regdt", "comment_writer")

