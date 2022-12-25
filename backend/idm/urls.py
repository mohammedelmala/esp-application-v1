from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet
from .myauth import CustomAuthToken

router = routers.DefaultRouter()
router.register("users", UserViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path('auth/', CustomAuthToken.as_view()),
]