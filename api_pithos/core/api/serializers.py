from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

from api_pithos.core.documents import EmployeeDocument
from api_pithos.core.documents import LeadDocument
from api_pithos.core.models import Employee
from api_pithos.core.models import Lead


class LeadDocumentSerializer(DocumentSerializer):
    class Meta:
        document = LeadDocument
        fields = (
            "id",
            "linkedin_url",
            "description",
            "n_employee",
            "raw_json",
            "company_name_linkedin",
            "url",
            "urn",
            "campaign_id",
        )


class EmployeeDocumentSerializer(DocumentSerializer):
    class Meta:
        document = EmployeeDocument
        fields = (
            "id",
            "first_name",
            "last_name",
            "urn",
            "raw_json",
            "lead",
        )


class LeadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = (
            "id",
            "linkedin_url",
            "description",
            "n_employee",
            "raw_json",
            "company_name_linkedin",
            "url",
            "urn",
            "campaign_id",
        )


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            "id",
            "first_name",
            "last_name",
            "urn",
            "raw_json",
            "lead",
        )


class LeadDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "__all__"


class EmployeeDetailSerializer(serializers.ModelSerializer):
    lead = LeadDetailSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = "__all__"
