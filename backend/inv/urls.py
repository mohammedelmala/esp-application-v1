from django.urls import path, include
from rest_framework import routers
from .views import BrandViewSet, CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register("brands", BrandViewSet)
router.register("categories", CategoryViewSet)
router.register("products", ProductViewSet)
urlpatterns = [
    path('', include(router.urls))
]