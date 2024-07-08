"""
Test the urls of the core app
"""

import pytest
from django.urls import resolve
from django.urls import reverse

from api_pithos.core.models import Employee
from api_pithos.core.models import Lead
from api_pithos.core.tests.factories import EmployeeFactory
from api_pithos.core.tests.factories import LeadFactory

pytestmark = pytest.mark.django_db


@pytest.fixture()
def lead() -> Lead:
    return LeadFactory()


@pytest.fixture()
def employee() -> Employee:
    return EmployeeFactory()


def test_lead_list():
    assert reverse("api:core:lead-list") == "/api/leads/"
    assert resolve("/api/leads/").view_name == "api:core:lead-list"


def test_lead_detail(lead: Lead):
    assert (
        reverse("api:core:lead-detail", kwargs={"pk": lead.pk})
        == f"/api/leads/{lead.pk}/"
    )
    assert resolve(f"/api/leads/{lead.pk}/").view_name == "api:core:lead-detail"
