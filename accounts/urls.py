from django.urls import path
from . import views
urlpatterns = [
    path("register/", views.register, name="register"),
    path("news/", views.news, name="news"),
    path("news/<int:news_id>/", views.news_detail, name="news_detail"),
]
