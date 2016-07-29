from django.shortcuts import render


def list(request):
    data = {}
    data['member_user'] = request.session["member_user"] if "member_user" in request.session.keys() else "GUEST"
    data['member_id'] = request.session["member_id"] if "member_id" in request.session.keys() else "1"
    return render(request, 'board/list.html', data)


def write(request):
    data = {}
    data['member_user'] = request.session["member_user"] if "member_user" in request.session.keys() else "GUEST"
    data['member_id'] = request.session["member_id"] if "member_id" in request.session.keys() else "1"
    return render(request, 'board/write.html', data)


def view(request, posting_id):
    data = {}
    data['member_user'] = request.session["member_user"] if "member_user" in request.session.keys() else "GUEST"
    data['member_id'] = request.session["member_id"] if "member_id" in request.session.keys() else "1"
    data["posting_id"] = posting_id

    return render(request, 'board/view.html', data)


def edit(request, posting_id):
    data = {}
    data['member_user'] = request.session["member_user"] if "member_user" in request.session.keys() else "GUEST"
    data['member_id'] = request.session["member_id"] if "member_id" in request.session.keys() else "1"
    data["posting_id"] = posting_id

    return render(request, 'board/edit.html', data)



