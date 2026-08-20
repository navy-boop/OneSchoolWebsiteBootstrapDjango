# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Message
from accounts.models import InviteCode


def message_submit(request):

    if request.method == "POST":

        invite_code = request.POST.get("invite_code")

        if not InviteCode.objects.filter(code=invite_code, is_used=False).exists():

            return JsonResponse({"success": False, "error": "邀请码错误，请重新输入！"})

        name = request.POST.get("name")
        email = request.POST.get("email")
        content = request.POST.get("content")

        Message.objects.create(name=name, email=email, content=content)

        return JsonResponse({"success": True})

    return JsonResponse({"success": False, "error": "请求方式错误"})
