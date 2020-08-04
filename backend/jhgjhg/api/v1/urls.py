from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import JHgjhgViewSet

router = DefaultRouter()
router.register("jhgjhg", JHgjhgViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
