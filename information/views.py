# Create your views here.
from django.shortcuts import render
from .models import PersonalInformation
def registration(request):
    if request.method == "POST":
        PersonalInformation.objects.create(
            name=request.POST.get("name"),
            gender=request.POST.get("gender"),
            age=request.POST.get("age"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            message=request.POST.get("message"),
        )
        return render(request, "success.html")
    return render(request, "PersonalInformationRegistration.html")
