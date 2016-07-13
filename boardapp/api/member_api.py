from config.constants import *
from member.models import *

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def member(request):
    response = {}

    if request.method == "POST":
        user = request.POST.get("userId")
        password = request.POST.get("password")

        if user is None or password is None:
            response["STS"] = ERR_USER_PARAM
            response["MSG"] = MSG[ERR_USER_PARAM]

            return JsonResponse(response)

        member = Member(user=user, password=password)
        member.save()

        response["STS"] = SUCCESS
        response["MSG"] = MSG[SUCCESS]
        response["DAT"] = member.id

        return JsonResponse(response)

    if request.method == "GET":
        user = request.GET.get("userId")
        password = request.GET.get("password")

        if user is None or password is None:
            response["STS"] = ERR_USER_PARAM
            response["MSG"] = MSG[ERR_USER_PARAM]

            return JsonResponse(response)

        member = Member.objects.filter(user=user, password=password)

        if not member:
            response["STS"] = ERR_DB_SELECT
            response["MSG"] = "Login Fail. Check user id and password"
        else:
            resData = {}
            resData["id"] = member[0].id
            resData["user"] = member[0].user

            response["STS"] = SUCCESS
            response["MSG"] = MSG[SUCCESS]
            response["DAT"] = resData

        return JsonResponse(response)

