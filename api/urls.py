from django.urls import path,include
from rest_framework import routers
from api import views

router=routers.DefaultRouter()
router.register(r'programers',views.ProgramerViewSet)

urlpatterns=[
    path('',include(router.urls))
]
