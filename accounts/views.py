from django.shortcuts import render
# Create your views here.
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import redirect, render
from .models import UserProfile
from .models import UserProfile, News
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
        # 检查是否同意协议
        if not agreement:
            return redirect("index")
        # 检查两次密码
        if password1 != password2:
            return redirect("index")
        # 检查用户名是否存在
        if User.objects.filter(username=username).exists():
            return redirect("index")
        # 保存用户
        with transaction.atomic():
            user = User.objects.create_user(
                username=username,
                password=password1
            )
            UserProfile.objects.create(
                user=user,
                role=role,
                email=email,
                age=age,
                phone=phone
            )
        return redirect("index")
    return redirect("index")
# 新闻中心
def news(request):
    news_list = News.objects.filter(
        is_published=True
    )
    return render(
        request,
        "school/news.html",
        {
            "news_list": news_list
        }
    )
def news_detail(request, news_id):
    news = News.objects.get(
        id=news_id,
        is_published=True
    )
    return render(
        request,
        "school/news_detail.html",
        {
            "news": news
        }
    )
# # -----------调试代码----------------------
# from django.contrib.auth.models import User
# from django.db import transaction
# from django.shortcuts import redirect
# from .models import UserProfile
# def register(request):
#     print("========== register 被调用 ==========")
#     print("请求方式：", request.method)
#     if request.method == "POST":
#         print("收到 POST 数据：")
#         print(request.POST)
#         role = request.POST.get("role")
#         username = request.POST.get("username")
#         phone = request.POST.get("phone")
#         password1 = request.POST.get("password1")
#         password2 = request.POST.get("password2")
#         agreement = request.POST.get("agreement")
#         print("role =", role)
#         print("username =", username)
#         print("phone =", phone)
#         print("password1 =", password1)
#         print("password2 =", password2)
#         print("agreement =", agreement)
#         # 检查是否同意协议
#         if not agreement:
#             print("错误：没有同意协议")
#             return redirect("index")
#         # 检查两次密码
#         if password1 != password2:
#             print("错误：两次密码不一致")
#             return redirect("index")
#         # 检查用户名是否存在
#         if User.objects.filter(username=username).exists():
#             print("错误：用户名已经存在")
#             return redirect("index")
#         # 保存用户
#         with transaction.atomic():
#             user = User.objects.create_user(
#                 username=username,
#                 password=password1
#             )
#             UserProfile.objects.create(
#                 user=user,
#                 role=role,
#                 phone=phone
#             )
#         print("========== 注册成功 ==========")
#         return redirect("index")
#     return redirect("index")