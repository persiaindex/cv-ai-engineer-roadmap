from django.db.models import Count

from .models import Alert, Inspection, Machine


def get_dashboard_summary() -> dict:
    return {
        "machine_count": Machine.objects.count(),
        "inspection_count": Inspection.objects.count(),
        "open_alert_count": Alert.objects.filter(is_open=True).count(),
        "defective_inspection_count": Inspection.objects.filter(status="defective").count(),
    }