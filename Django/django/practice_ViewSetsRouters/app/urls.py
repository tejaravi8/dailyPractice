from rest_framework.routers import DefaultRouter
from .views import StudentViewSet
from django.urls import include,path

router = DefaultRouter()
router.register('student',StudentViewSet)

urlpatterns = router.urls

# anything is fine upper or lower

# urlpatterns = [
#     path('', include(router.urls)),
# ]