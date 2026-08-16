from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path(
    "about-school/",
    views.school_profile,
    name="school_profile"
),
]
