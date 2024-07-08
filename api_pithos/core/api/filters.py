from django.contrib.postgres.search import SearchVector
from django_filters import rest_framework as filters

from api_pithos.core.models import Employee
from api_pithos.core.models import Lead


class LeadFilter(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")

    class Meta:
        model = Lead
        fields = {
            "n_employee": ["exact", "lt", "lte", "gt", "gte"],
            "company_name_linkedin": ["exact", "icontains"],
        }

    def search_filter(self, queryset, name, value):
        return queryset.annotate(
            search=SearchVector("linkedin_url", "description", "company_name_linkedin")
        ).filter(search__icontains=value)


class EmployeeFilter(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")

    class Meta:
        model = Employee
        exclude = ["raw_json"]

    def search_filter(self, queryset, name, value):
        return queryset.annotate(
            search=SearchVector(
                "first_name",
                "last_name",
            )
        ).filter(search__icontains=value)
