from .models import Student
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    
    # output = "<h1>Products</h1>"

    # for p in products:
    #     output += f"<li>{p.name} - {p.age} - {p.email}</li>"

    # return HttpResponse(output)