from django.http import HttpResponse,JsonResponse
from .models import Student
from django.shortcuts import render,redirect,get_object_or_404
import json
from django.views.decorators.csrf import csrf_exempt

def student_list(request):
    students = Student.objects.all()
    return render(request,"index.html",{"Students":students})
    # data=list(students.values())
    # return JsonResponse(data,safe=False)

@csrf_exempt
def add_student(request):
    if request.method=="POST":
        body=json.loads(request.body)
        
        name=body.get("name")
        age=body.get("age")
        email=body.get("email")
        
        Student.objects.create(
            name=name,
            age=age,
            email=email
        )
        return JsonResponse({"message":"student added successfully"})
    
    return JsonResponse({"message":"add_student.html"})
    # if request.method =="POST":
    #     name = request.POST.get('name')
    #     age = request.POST.get('age')
    #     email = request.POST.get('email')
        
    #     if not name or not age or not email:
    #         return render(request, 'add_student.html', {'error': 'All fields required'})
        
    #     Student.objects.create(
    #         name=name,
    #         age=age,
    #         email=email
    #     )
    #     return redirect("home")
    
    # return render(request, 'add_student.html')
@csrf_exempt
def delete_student(request,id):
    if request.method=="DELETE":
        student=get_object_or_404(Student,id=id)
        student.delete()
        return JsonResponse({"message":"Student Deleted successfully"})
    return JsonResponse({"message":"delete function executed"})
    # student=get_object_or_404(Student,id=id)
    # student.delete()
    # return redirect("home")

@csrf_exempt
def update_student(request,id):
    # stu=get_object_or_404(Student,id=id)
    
    if request.method=="PUT":
        try:
            body = json.loads(request.body)

            product = get_object_or_404(Student, id=id)

            product.name = body.get('name', product.name)
            product.age = body.get('age', product.age)
            product.email = body.get('email', product.email)

            product.save()

            return JsonResponse({"message": "Updated successfully"})

        except Exception as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Only PUT allowed"})
        
    # if request.method=="POST":
    #     stu.name=request.POST.get('name')
    #     stu.age=request.POST.get('age')
    #     stu.email=request.POST.get('email')
    #     stu.save()
        
    #     return redirect("home")
    # return render(request,"update_student.html",{"students":stu})

# def studentt_detail(request,id):
#     students=get_object_or_404(Student,id=id)
    
#     data={
#         "id":students.id,
#         "name":students.name,
#         "age":students.age,
#         "email":students.email
#     }
#     return JsonResponse(data)

def student_detail(request):
    if request.method=="POST":
        ag=request.POST.get("age")
        
        student=Student.objects.filter(age__gt=ag)
        data=list(student.values())
        return JsonResponse(data,safe=False)
        # return render(request,"index.html",{"Students":student})
    return render(request,"filter.html")


    # output = "<h1>Products</h1>"

    # for p in products:
    #     output += f"<li>{p.name} - {p.age} - {p.email}</li>"

    # return HttpResponse(output)