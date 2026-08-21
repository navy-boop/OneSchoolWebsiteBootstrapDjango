from django.urls import path
from . import views

urlpatterns = [
    # 新闻中心
    
    path("", views.news_list, name="news"),
    # 新闻详情
    path("<int:id>/", views.news_detail, name="news_detail"),
    path("notice/<int:id>/", views.notice_detail, name="notice_detail"),
]


# ----------------------------------------------------
