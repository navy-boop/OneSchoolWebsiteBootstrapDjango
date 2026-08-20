from django.shortcuts import render, get_object_or_404
from .models import News
from .models import Notice


# 新闻中心列表
def news_list(request):

    news_list = News.objects.all().order_by("-publish_date")

    context = {
        "news_list": news_list,
    }

    return render(request, "news/news_list.html", context)


# ------------------------------------------------------------------


# 新闻详情
def news_detail(request, id):

    news = get_object_or_404(News, id=id)

    context = {
        "news": news,
    }

    return render(request, "news/news_detail.html", context)


# ----------------------------------------------------


def notice_detail(request, id):

    notice = get_object_or_404(Notice, id=id)

    return render(request, "news/notice_detail.html", {"notice": notice})
