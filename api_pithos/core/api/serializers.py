from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from api_pithos.core.documents import EmployeeDocument
from api_pithos.core.documents import LeadDocument


class LeadDocumentSerializer(DocumentSerializer):
    class Meta:
        document = LeadDocument
        fields = (
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
            "first_name",
            "last_name",
            "urn",
            "raw_json",
        )
