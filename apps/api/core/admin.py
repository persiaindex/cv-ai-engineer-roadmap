from django.contrib import admin

from .models import Alert, Feeder, Inspection, Machine,  MLPrediction

admin.site.register(MLPrediction)


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ("machine_id", "name", "location", "is_active", "created_at")
    search_fields = ("machine_id", "name", "location")
    list_filter = ("is_active", "location")


@admin.register(Feeder)
class FeederAdmin(admin.ModelAdmin):
    list_display = ("feeder_id", "machine", "material_type", "fill_level", "created_at")
    search_fields = ("feeder_id", "machine__machine_id", "material_type")
    list_filter = ("material_type",)


@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display = ("inspection_id", "machine", "defect_score", "status", "created_at")
    search_fields = ("inspection_id", "machine__machine_id", "status")
    list_filter = ("status",)


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ("alert_id", "source_type", "source_id", "severity", "is_open", "created_at")
    search_fields = ("alert_id", "source_type", "source_id", "severity")
    list_filter = ("severity", "is_open")