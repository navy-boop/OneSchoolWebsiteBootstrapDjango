from django.shortcuts import render
from .models import PersonalInformation
from accounts.models import InviteCode


def registration(request):

    if request.method == "POST":

        invite_code = request.POST.get("invite_code")

        if not InviteCode.objects.filter(code=invite_code).exists():

            return render(
                request,
                "PersonalInformationRegistration.html",
                {"error": "邀请码错误！"},
            )

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
