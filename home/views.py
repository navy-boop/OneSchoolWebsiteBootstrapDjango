# Create your views here.
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def school_profile(request):
    return render(request, "school_profile.html")
def moral_education(request):
    return render(request, "MoralEducation.html")
def teaching_research(request):
    return render(request, "TeachingResearch.html")
