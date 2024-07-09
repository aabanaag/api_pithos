"""
Core - services
"""

from datetime import UTC
from datetime import datetime

from django.http import HttpResponse
from tablib import Dataset

from api_pithos.core.admin import EmployeeResource
from api_pithos.core.admin import LeadResource


def export_leads(ids: list) -> Dataset:
    queryset = LeadResource().get_queryset().filter(id__in=ids)
    return LeadResource().export(queryset)


def export_employees(ids: list) -> Dataset:
    queryset = EmployeeResource().get_queryset().filter(id__in=ids)
    return EmployeeResource().export(queryset)


def export_to_csv(ids: list, model: str) -> HttpResponse:
    if model == "lead":
        dataset = export_leads(ids)
    elif model == "employee":
        dataset = export_employees(ids)
    else:
        msg = f"Model {model} is not supported"
        raise ValueError(msg)

    response = HttpResponse(dataset, content_type="text/csv")
    today = datetime.now(UTC).strftime("%Y-%m-%d")
    filename = f"{model}-{today}.csv"
    response["Content-Disposition"] = f"attachment; {filename}"

    return response
