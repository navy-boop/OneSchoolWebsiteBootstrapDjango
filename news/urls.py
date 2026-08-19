# from django.urls import path
# from . import views
# urlpatterns = [
#     path("", views.news_list, name="news"),
# ]
from django.urls import path
from . import views
urlpatterns = [
    path("", views.news, name="news"),
    path("<int:news_id>/", views.news_detail, name="news_detail"),
]
