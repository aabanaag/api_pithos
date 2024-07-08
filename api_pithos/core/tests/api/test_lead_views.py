"""
Core - Lead views
"""

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api_pithos.core.tests.factories import LeadFactory
from api_pithos.users.tests.factories import UserFactory


@pytest.mark.django_db()
class TestLeadViews(APITestCase):
    def setUp(self):
        super().setUp()

        self.lead = LeadFactory.create(description="A description")
        self.user = UserFactory.create()

    def test_should_not_allow_unauthenticated_users_to_list_leads(self):
        response = self.client.get(reverse("api:core:lead-list"))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_should_allow_authenticated_users_to_list_leads(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("api:core:lead-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_allow_create_lead(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            reverse("api:core:lead-list"),
            data={
                "linkedin_url": "https://www.linkedin.com/in/johndoe",
                "description": "A description",
                "n_employee": 10,
                "company_name_linkedin": "John Doe",
                "url": "https://www.example.com",
                "urn": "urn:uuid:123456",
                "raw_json": {"key": "value"},
                "campaign_id": "123456",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data["linkedin_url"],
            "https://www.linkedin.com/in/johndoe",
        )

    def test_should_allow_retrieve_lead(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse("api:core:lead-detail", kwargs={"pk": self.lead.pk}),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["linkedin_url"], self.lead.linkedin_url)

    def test_should_search_leads(self):
        self.client.force_authenticate(user=self.user)

        LeadFactory.create(description="Please describe")
        LeadFactory.create()

        url = reverse("api:core:lead-list")
        url = f"{url}?search=desc"

        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        count = response.json()["count"]

        self.assertEqual(count, 2)

        descriptions = [lead["description"] for lead in response.json()["results"]]
        self.assertIn("A description", descriptions)

    def test_should_filter_leads_by_n_employee(self):
        self.client.force_authenticate(user=self.user)

        LeadFactory.create(n_employee=10)
        LeadFactory.create(n_employee=20)

        url = reverse("api:core:lead-list")
        url = f"{url}?n_employee=10"

        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        count = response.json()["count"]

        self.assertEqual(count, 1)

        n_employees = [lead["n_employee"] for lead in response.json()["results"]]
        self.assertIn(10, n_employees)

    def test_should_filter_by_company_name(self):
        self.client.force_authenticate(user=self.user)

        LeadFactory.create(company_name_linkedin="acme")
        LeadFactory.create(company_name_linkedin="numi")

        url = reverse("api:core:lead-list")
        url = f"{url}?company_name_linkedin=numi"

        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        count = response.json()["count"]

        self.assertEqual(count, 1)

        company_names = [
            lead["company_name_linkedin"] for lead in response.json()["results"]
        ]
        self.assertIn("numi", company_names)
