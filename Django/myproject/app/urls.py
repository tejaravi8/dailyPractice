from django.urls import path
from .views import home,about,skills,add_skill,user_login,signup

urlpatterns = [
    path("",home),
    path("about/",about),
    path("skills/",skills),
    path("add_skill/",add_skill),
    path("login/",user_login),
    path("signup/",signup),
]
