from .views import student_list,add_student,delete_student,update_student,student_detail
from django.urls import path

urlpatterns = [
    path("",student_list,name="home"),
    path("add_student/",add_student,name="add_student"),
    path('delete/<int:id>/', delete_student, name='delete_student'),
    path("update_student/<int:id>/",update_student,name="update"),
    path("filter/",student_detail,name="detail"),
]
