from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from api_pithos.core.api.serializers import LeadDocumentSerializer
from api_pithos.core.documents import LeadDocument


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
