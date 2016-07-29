from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from config.constants import *
from models import Board
from serializers import BoardListSerializer



@api_view(['GET', 'POST'])
def board(request):
    response = {}
    result = {}

    if request.method == "POST":
        member_id = request.data["memberId"]
        title = request.data["title"]
        content = request.data["content"]

        if member_id is None or title is None or content is None:
            response["STS"] = ERR_USER_PARAM
            response["MSG"] = MSG[ERR_USER_PARAM]

            return Response(response)

        board = Board(member_id=member_id, title=title, content=content)
        board.save()

        response["STS"] = SUCCESS
        response["MSG"] = MSG[SUCCESS]
        response["DAT"] = board.id

        return Response(response)

    if request.method == "GET":
        paginator = PageNumberPagination()

        board_list = Board.objects.order_by("-id").all()
        result_page = paginator.paginate_queryset(board_list, request)
        board_list_serializer = BoardListSerializer(result_page, many=True)

        result["board_list"] = board_list_serializer.data
        result["total_cnt"] = len(board_list)

        response["STS"] = SUCCESS
        response["MSG"] = MSG[SUCCESS]
        response["DAT"] = result

        return Response(response)


@api_view(['GET', 'DELETE', "PUT"])
def board_detail(request, id):
    response = {}
    result = {}

    if request.method == "GET":

        posting = Board.objects.get(id=id)
        posting_serializer = BoardListSerializer(posting)

        result["posting"] = posting_serializer.data

        response["STS"] = SUCCESS
        response["MSG"] = MSG[SUCCESS]
        response["DAT"] = result

        return Response(response)

    if request.method == "DELETE":
        result["id"] = id

        posting = Board.objects.filter(id=id)

        if len(posting) != 1:
            response["STS"] = ERR_DB_DELETE
            response["MSG"] = MSG[ERR_DB_DELETE]
            response["DAT"] = result
        else :
            posting[0].delete()
            response["STS"] = SUCCESS
            response["MSG"] = MSG[SUCCESS]
            response["DAT"] = result

        return Response(response)


    if request.method == "PUT":
        result["id"] = id

        member = request.data["memberId"]
        posting_id = request.data["postingId"]
        title = request.data["title"]
        content = request.data["content"]

        posting = Board.objects.filter(id=posting_id, member=member)

        if id != posting_id:
            response["STS"] = ERR_DB_UPDATE
            response["MSG"] = MSG[ERR_DB_UPDATE]
            response["DAT"] = result

            return Response(response)

        if len(posting) != 1:
            response["STS"] = ERR_DB_UPDATE
            response["MSG"] = MSG[ERR_DB_UPDATE]
            response["DAT"] = result

            return Response(response)
        else:
            posting = posting[0]

        posting.title = title
        posting.content = content
        posting.moddt = datetime.now()

        posting.save()

        response["STS"] = SUCCESS
        response["MSG"] = MSG[SUCCESS]
        response["DAT"] = result

        return Response(response)


