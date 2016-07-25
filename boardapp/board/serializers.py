from rest_framework import serializers
from models import Board


class BoardListSerializer(serializers.ModelSerializer):
    writer = serializers.CharField(source="member.user", read_only=True)

    class Meta:
        model = Board
        fields = ("id", "title", "content", "view_cnt", "regdt", "member",  "writer")
