from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AlertViewSet, FeederViewSet, InspectionViewSet, MachineViewSet, dashboard_summary

router = DefaultRouter()
router.register("machines", MachineViewSet)
router.register("feeders", FeederViewSet)
router.register("inspections", InspectionViewSet)
router.register("alerts", AlertViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("dashboard/summary/", dashboard_summary, name="dashboard-summary"),
]