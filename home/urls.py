from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about-school/", views.school_profile, name="school_profile"),
    path(
        "information_registration/",
        views.personal_information_registration,
        name="information_registration",
    ),
    path("temp_home/", views.temp_home, name="temp_home"),
    path("school-intro/", views.school_intro, name="school_intro"),
    path("beautiful_animation/", views.beautiful_animation, name="beautiful_animation"),
]
