from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api_pithos.core.api.filters import LeadFilter
from api_pithos.core.api.serializers import EmployeeDetailSerializer
from api_pithos.core.api.serializers import EmployeeListSerializer
from api_pithos.core.api.serializers import LeadDetailSerializer
from api_pithos.core.api.serializers import LeadDocumentSerializer
from api_pithos.core.api.serializers import LeadListSerializer
from api_pithos.core.documents import LeadDocument
from api_pithos.core.models import Employee
from api_pithos.core.models import Lead


class LeadDocumentViewSet(DocumentViewSet):
    document = LeadDocument
    serializer_class = LeadDocumentSerializer
    filter_backends = [
        SearchFilterBackend,
    ]
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
    suggester_fields = {
        "linkedin_url": {
            "field": "linkedin_url.suggest",
            "suggesters": [
                SUGGESTER_COMPLETION,
            ],
        },
        "description": {
            "field": "description.suggest",
            "suggesters": [
                SUGGESTER_COMPLETION,
            ],
        },
        "raw_json": {
            "field": "raw_json.suggest",
            "suggesters": [
                SUGGESTER_COMPLETION,
            ],
        },
    }


class LeadViewSet(ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = LeadFilter

    def get_serializer_class(self):
        if self.action in ["list", "create", "update"]:
            return LeadListSerializer
        return LeadDetailSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["list", "create", "update"]:
            return EmployeeListSerializer
        return EmployeeDetailSerializer
