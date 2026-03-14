from django.urls import path
from .views import home,about,skills,add_skill

urlpatterns = [
    path("",home),
    path("about/",about),
    path("skills/",skills),
    path("add_skill/",add_skill),
]
