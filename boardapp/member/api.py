from rest_framework.decorators import api_view
from rest_framework.response import Response

from config.constants import *
from models import Member

@api_view(['GET', 'POST'])
def member(request):
    response = {}

    if request.method == "POST":
        user = request.data["userId"]
        password = request.data["password"]

        if user is None or password is None:
            response["STS"] = ERR_USER_PARAM
            response["MSG"] = MSG[ERR_USER_PARAM]

            return Response(response)

        member = Member(user=user, password=password)
        member.save()

        response["STS"] = SUCCESS
        response["MSG"] = MSG[SUCCESS]
        response["DAT"] = member.id

        return Response(response)

    if request.method == "GET":
        user = request.query_params["userId"]
        password = request.query_params["password"]

        if user is None or password is None:
            response["STS"] = ERR_USER_PARAM
            response["MSG"] = MSG[ERR_USER_PARAM]

            return Response(response)

        member = Member.objects.filter(user=user, password=password)

        if not member:
            response["STS"] = ERR_DB_SELECT
            response["MSG"] = "Login Fail. Check user id and password"
        else:
            resData = {}
            resData["id"] = member[0].id
            resData["user"] = member[0].user

            request.session["login"] = True
            request.session["member_id"] = member[0].id
            request.session["member_user"] = member[0].user

            response["STS"] = SUCCESS
            response["MSG"] = MSG[SUCCESS]
            response["DAT"] = resData

            return Response(response)









