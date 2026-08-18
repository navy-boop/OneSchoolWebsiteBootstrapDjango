# Create your views here.
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def school_profile(request):
    return render(request, "school_profile.html")
def personal_information_registration(request):
    return render(
        request,
        'PersonalInformationRegistration.html'
    )
def temp_home(request):
    return render(request, "temp_home.html")