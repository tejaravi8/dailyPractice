from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Skills
from django.contrib import messages
from .forms import SkillForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
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

@login_required
def skills(request):
    skills=Skills.objects.all()
    context={"skills":skills}
    
    return render(request,"app/skills.html",context)

def add_skill(request):

    if request.method == "POST":
        form = SkillForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Skill added successfully")
            return redirect("/skills")

    else:
        form = SkillForm()

    return render(request, "app/add_skill.html", {"form": form})

@login_required
def user_login(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/home/")

    return render(request, "app/login.html")

def signup(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/home")

    else:
        form = UserCreationForm()

    return render(request, "app/signup.html", {"form": form})