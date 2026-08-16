# Create your views here.
from django.shortcuts import render, redirect
from .models import Message
def message_submit(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        content = request.POST.get("content")
        Message.objects.create(
            name=name,
            email=email,
            content=content
        )
        return redirect("index")
    return redirect("index")