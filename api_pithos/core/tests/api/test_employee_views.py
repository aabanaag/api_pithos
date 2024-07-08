"""
Core - Employee views
"""

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api_pithos.core.tests.factories import EmployeeFactory
from api_pithos.core.tests.factories import LeadFactory
from api_pithos.users.tests.factories import UserFactory


@pytest.mark.django_db()
class TestEmployeeViews(APITestCase):
    def setUp(self):
        super().setUp()

        self.lead = LeadFactory.create()
        self.employee = EmployeeFactory.create(lead=self.lead)
        self.user = UserFactory.create()

    def test_should_not_allow_unauthenticated_users_to_list_employees(self):
        response = self.client.get(reverse("api:core:employee-list"))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_should_allow_authenticated_users_to_list_employees(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("api:core:employee-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_allow_create_employee(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            reverse("api:core:employee-list"),
            data={
                "first_name": "John",
                "last_name": "Doe",
                "lead": self.lead.id,
                "urn": "urn:uuid:123456",
                "raw_json": {"key": "value"},
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["first_name"], "John")
        self.assertEqual(response.data["last_name"], "Doe")

    def test_should_allow_retrieve_employee(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse("api:core:employee-detail", kwargs={"pk": self.employee.pk}),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], self.employee.first_name)
        self.assertEqual(response.data["last_name"], self.employee.last_name)

        lead = response.data["lead"]

        self.assertEqual(lead["id"], self.lead.id)
        self.assertEqual(lead["linkedin_url"], self.lead.linkedin_url)
