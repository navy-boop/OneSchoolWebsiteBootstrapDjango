from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import transaction
from django.http import JsonResponse
from .models import UserProfile
from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings
from .models import UserProfile, InviteCode


def register(request):
    if request.method == "POST":
        role = request.POST.get("role")
        username = request.POST.get("username")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        age = request.POST.get("age")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        agreement = request.POST.get("agreement")
        # ===== 邀请码验证开始 =====

        invite_code = request.POST.get("invite_code")

        if not InviteCode.objects.filter(
            code=invite_code,
        ).exists():

            return JsonResponse(
                {"success": False, "error": "邀请码错误，请输入正确的邀请码！"}
            )

        # ===== 邀请码验证结束 =====
        # 用来保存所有错误
        errors = {}
        # 检查是否同意注册协议
        if not agreement:
            errors["agreement"] = "请先同意注册协议。"
        # 检查两次密码是否一致
        if password1 != password2:
            errors["password"] = "两次输入的密码不一致。"
        # 检查用户名是否已经存在
        if User.objects.filter(username=username).exists():
            errors["username"] = "用户名已经存在，请修改用户名。"
        # 如果存在任何错误，一次性返回所有错误
        if errors:
            return JsonResponse({"success": False, "errors": errors})
        # 保存用户

        # ------------------------------------------------------------------------------------------------------

        with transaction.atomic():

            user = User.objects.create_user(username=username, password=password1)

            UserProfile.objects.create(
                user=user, role=role, email=email, age=age, phone=phone
            )

        return JsonResponse({"success": True})
    # -----------------------------------------------------------------------------------------

    return JsonResponse({"success": False, "error": "请求方式错误。"})


# 注册成功页面
def register_success(request):
    return render(request, "success.html")


# 新增 Django 检查接口，与邀请码有关


def check_invite(request):

    invite_code = request.POST.get("invite_code")

    exists = InviteCode.objects.filter(
        code=invite_code,
    ).exists()

    return JsonResponse({"valid": exists})


# ----------------------------------------------------------------------


def login_page(request):

    return render(request, "Login_Page.html")
