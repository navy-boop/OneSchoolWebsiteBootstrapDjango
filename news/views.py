from django.shortcuts import render
from .models import News
def news(request):
    news_list = News.objects.all()
    return render(request, "news/news.html", {"news_list": news_list})
def news_detail(request, news_id):
    news = News.objects.get(id=news_id)
    return render(request, "news/news_detail.html", {"news": news})
