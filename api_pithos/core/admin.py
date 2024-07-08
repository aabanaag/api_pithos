# Register your models here.
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from api_pithos.core.models import Employee
from api_pithos.core.models import Lead


class LeadResource(resources.ModelResource):
    class Meta:
        model = Lead


class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee


@admin.register(Lead)
class LeadAdmin(ImportExportModelAdmin):
    resource_class = LeadResource
    list_display = (
        "linkedin_url",
        "n_employee",
        "campaign_id",
    )
    search_fields = (
        "linkedin_url",
        "description",
        "n_employee",
        "raw_json",
        "company_name_linkedin",
        "url",
        "urn",
        "campaign_id",
    )


@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = EmployeeResource
    list_display = (
        "first_name",
        "last_name",
    )
    search_fields = (
        "first_name",
        "last_name",
    )
