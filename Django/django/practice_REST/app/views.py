from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET',"PUT","DELETE"])
def student_api(request,id):
    student=get_object_or_404(Student,id=id)
    
    if request.method=="GET":
        serializer=StudentSerializer(student)
        return Response({"data":serializer.data})
    
    elif request.method=="PUT":
        serializer=StudentSerializer(student, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method=="DELETE":
        student.delete()
        return Response({"message":"Deleted successfully"})

@csrf_exempt
@api_view(["POST"])
def post_student(request):
    if request.method=="POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        
    
    # if request.method=="GET":
    #     student=Student.objects.all()
    #     serializer=StudentSerializer(student,many=True)
    #     return Response(serializer.data)
    
    # if request.method=="POST":
    #     serializer=StudentSerializer(data=request.data)
        
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)
    
    
# def student_list(request):
#     students = Student.objects.all()
#     return render(request,"index.html",{"Students":students})


# def add_student(request):
#     if request.method =="POST":
#         name = request.POST.get('name')
#         age = request.POST.get('age')
#         email = request.POST.get('email')
        
#         if not name or not age or not email:
#             return render(request, 'add_student.html', {'error': 'All fields required'})
        
#         Student.objects.create(
#             name=name,
#             age=age,
#             email=email
#         )
#         return redirect("home")
    
#     return render(request, 'add_student.html')

# def delete_student(request,id):
#     student=get_object_or_404(Student,id=id)
#     student.delete()
#     return redirect("home")

# def update_student(request,id):
#     stu=get_object_or_404(Student,id=id)
    
#     if request.method=="POST":
#         stu.name=request.POST.get('name')
#         stu.age=request.POST.get('age')
#         stu.email=request.POST.get('email')
#         stu.save()
        
#         return redirect("home")
#     return render(request,"update_student.html",{"students":stu})
        
    
#     # output = "<h1>Products</h1>"

#     # for p in products:
#     #     output += f"<li>{p.name} - {p.age} - {p.email}</li>"

#     # return HttpResponse(output)