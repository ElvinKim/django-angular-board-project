from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def join(request):
    return render(request, 'member/join.html', {})

def login(request):
    if "member_user" in request.session.keys():
        return redirect("/board/list")

    return render(request, 'member/login.html', {})


def logout(request):
    del request.session["login"]
    del request.session["member_id"]
    del request.session["member_user"]

    return redirect("/member/login")
