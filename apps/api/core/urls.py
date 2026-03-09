from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AlertViewSet, FeederViewSet, InspectionViewSet, MachineViewSet

router = DefaultRouter()
router.register("machines", MachineViewSet)
router.register("feeders", FeederViewSet)
router.register("inspections", InspectionViewSet)
router.register("alerts", AlertViewSet)

urlpatterns = [
    path("", include(router.urls)),
]