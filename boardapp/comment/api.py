from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from config.constants import *
from models import Comment
from serializers import CommentListSerializer


@api_view(['GET', 'POST'])
def comment_list(request):
    response = {}
    result = {}

    if request.method == "POST":
        member_id = request.data["memberId"]
        board_id = request.data["boardId"]
        comment = request.data["comment"]

        if member_id is None or comment is None:
            response["STS"] = ERR_USER_PARAM
            response["MSG"] = MSG[ERR_USER_PARAM]

            return Response(response)

        comment = Comment(board_id=board_id, member_id=member_id, comment=comment)
        comment.save()

        result["id"] = comment.id
        result["comment"] = comment.comment
        result["regdt"] = comment.regdt

        response["STS"] = SUCCESS
        response["MSG"] = MSG[SUCCESS]
        response["DAT"] = result

        return Response(response)

    if request.method == "GET":
        paginator = PageNumberPagination()

        board_list = Comment.objects.order_by("-id").all()
        result_page = paginator.paginate_queryset(board_list, request)
        comment_list_serializer = CommentListSerializer(result_page, many=True)

        result["comment_list"] = comment_list_serializer.data
        result["total_cnt"] = len(board_list)

        response["STS"] = SUCCESS
        response["MSG"] = MSG[SUCCESS]
        response["DAT"] = result

        return Response(response)

