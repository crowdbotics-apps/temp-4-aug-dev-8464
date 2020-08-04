from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import HgjhViewSet

router = DefaultRouter()
router.register("hgjh", HgjhViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
