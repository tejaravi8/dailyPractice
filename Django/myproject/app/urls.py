from django.urls import path
from .views import home,about,skills

urlpatterns = [
    path("",home),
    path("about/",about),
    path("skills/",skills),
]
