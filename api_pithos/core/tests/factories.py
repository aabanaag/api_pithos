"""
Core factories
"""

from factory import Faker
from factory import SubFactory
from factory.django import DjangoModelFactory

from api_pithos.core.models import Employee
from api_pithos.core.models import Lead


class LeadFactory(DjangoModelFactory):
    linkedin_url = Faker("url")
    description = Faker("text")
    n_employee = Faker("random_int", min=1, max=100)
    raw_json = Faker("json")
    company_name_linkedin = Faker("company")
    url = Faker("url")
    urn = Faker("uuid4")
    campaign_id = Faker("uuid4")

    class Meta:
        model = Lead


class EmployeeFactory(DjangoModelFactory):
    lead = SubFactory(LeadFactory)
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    urn = Faker("uuid4")
    raw_json = Faker("json")

    class Meta:
        model = Employee
