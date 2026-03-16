from django.contrib import admin
from .models import BriefResponse


@admin.register(BriefResponse)
class BriefResponseAdmin(admin.ModelAdmin):
    list_display = ("company_name", "full_name", "email", "project_type", "created_at")
    list_filter = ("project_type", "design_style", "content_ready", "created_at")
    search_fields = ("company_name", "full_name", "email")