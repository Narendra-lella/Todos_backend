from django.urls import path,include
from .views import todos,TodoAPIViewSet

from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'todos',TodoAPIViewSet,basename="todos")

urlpatterns = [
    path('', include(router.urls)), 
    path('helow',todos,name="helow"),

    
]
