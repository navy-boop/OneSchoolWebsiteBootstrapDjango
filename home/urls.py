from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path(
    "about-school/",
    views.school_profile,
    name="school_profile"
    path('information_registration/', 
         views.personal_information_registration, 
         name='information_registration'),
),
]
