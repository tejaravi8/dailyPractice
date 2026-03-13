from django.shortcuts import render
from django.http import HttpResponse
from .models import Skills

def home(request):
    data={
        "username":"Teja",
        "course":"Django",
        "day":"Thursday"
    }
    return render(request,"app/home.html",data)
    # return HttpResponse("hello this is revision")

def about(request):
    return render(request,"app/about.html")
    # return HttpResponse("Hey this is about page")

def skills(request):
    
    skills=Skills.objects.get(id=1)
    context={"skills":skills}
    
    return render(request,"app/skills.html",context)
