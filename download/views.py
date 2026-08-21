

# Create your views here.
from django.shortcuts import render
from .models import DownloadFile


def download_list(request):

    files = DownloadFile.objects.all()

    return render(request, "download/download_list.html", {"files": files})
