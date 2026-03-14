from django.shortcuts import render,redirect
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
    
    skills=Skills.objects.all()
    context={"skills":skills}
    
    return render(request,"app/skills.html",context)

def add_skill(request):
    
    if request.method=="POST":
        name=request.POST.get("name")
        level=request.POST.get("level")
        experience=request.POST.get("experience")
        
        Skills.objects.create(name=name,level=level,experience=experience)
        
        return redirect("/skills/")
    return render(request, "app/add_skill.html")