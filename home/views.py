# Create your views here.
from django.shortcuts import render


from news.models import News
from news.models import Notice


def school_profile(request):
    return render(request, "school_profile.html")


def personal_information_registration(request):
    return render(request, "PersonalInformationRegistration.html")


def temp_home(request):
    return render(request, "temp_home.html")


# --------------------------------------------


# ------------------------------------


def index(request):

    news_list = News.objects.all()[:5]

    notice_list = Notice.objects.all()[:5]

    return render(
        request,
        "index.html",
        {
            "news_list": news_list,
            "notice_list": notice_list,
        },
    )
