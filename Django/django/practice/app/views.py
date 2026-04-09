from django.http import HttpResponse
from .models import Student
from django.shortcuts import render,redirect,get_object_or_404

def student_list(request):
    students = Student.objects.all()
    return render(request,"index.html",{"Students":students})
    
def add_student(request):
    if request.method =="POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        
        if not name or not age or not email:
            return render(request, 'add_student.html', {'error': 'All fields required'})
        
        Student.objects.create(
            name=name,
            age=age,
            email=email
        )
        return redirect("home")
    
    return render(request, 'add_student.html')

def delete_student(request,id):
    student=get_object_or_404(Student,id=id)
    student.delete()
    return redirect("home")

def update_student(request,id):
    stu=get_object_or_404(Student,id=id)
    
    if request.method=="POST":
        stu.name=request.POST.get('name')
        stu.age=request.POST.get('age')
        stu.email=request.POST.get('email')
        stu.save()
        
        return redirect("home")
    return render(request,"update_student.html",{"students":stu})
        
    
    # output = "<h1>Products</h1>"

    # for p in products:
    #     output += f"<li>{p.name} - {p.age} - {p.email}</li>"

    # return HttpResponse(output)