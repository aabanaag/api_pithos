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

        self.lead = LeadFactory.create()
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
