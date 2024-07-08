from django.contrib.postgres.search import SearchVector
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import CharField
from django.db.models import Q
from django.db.models.functions import Cast
from django.db.models.functions import Greatest
from django_filters import rest_framework as filters

from api_pithos.core.models import Lead


class LeadFilter(filters.FilterSet):
    search = filters.CharFilter(method="filter_search")

    class Meta:
        model = Lead
        fields = (
            "linkedin_url",
            "n_employee",
            "company_name_linkedin",
            "url",
            "urn",
            "campaign_id",
        )

    def filter_search(self, queryset, name, value):
        search_fields = [
            "linkedin_url",
            "description",
            "company_name_linkedin",
            "url",
            "urn",
            "campaign_id",
        ]

        search_conditions = []
        for criteria in search_fields:
            search_conditions.extend(
                [
                    TrigramSimilarity(criteria, value),
                ]
            )

        return (
            queryset.annotate(
                similarity=Greatest(*search_conditions),
                search=SearchVector(Cast("n_employee", CharField())),
            )
            .filter(Q(similarity__gt=0.2) | Q(search__icontains=value))
            .order_by("-similarity")
        )
