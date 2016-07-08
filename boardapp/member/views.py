from django.shortcuts import render

# Create your views here.

def join(request):
    return render(request, 'member/join.html', {})

def login(request):
    return render(request, 'member/login.html', {})
