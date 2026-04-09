from .views import student_api,post_student
from django.urls import path

urlpatterns = [
    path("<int:id>/",student_api),
    path("add/",post_student)
    
    
    # path("add_student/",add_student,name="add_student"),
    # path('delete/<int:id>/', delete_student, name='delete_student'),
    # path("update_student/<int:id>/",update_student,name="update"),
]
