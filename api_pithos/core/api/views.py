from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api_pithos.core.api.filters import EmployeeFilter
from api_pithos.core.api.filters import LeadFilter
from api_pithos.core.api.serializers import EmployeeDetailSerializer
from api_pithos.core.api.serializers import EmployeeListSerializer
from api_pithos.core.api.serializers import ExportSerializer
from api_pithos.core.api.serializers import LeadDetailSerializer
from api_pithos.core.api.serializers import LeadListSerializer
from api_pithos.core.models import Employee
from api_pithos.core.models import Lead
from api_pithos.core.services import export_to_csv


class LeadViewSet(ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = LeadFilter
    filter_backends = (DjangoFilterBackend,)

    def get_serializer_class(self):
        if self.action in ["list", "create", "update"]:
            return LeadListSerializer
        return LeadDetailSerializer

    @action(detail=False, methods=["post"], url_path="export")
    def export_lead(self, request):
        serializer = ExportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return export_to_csv(ids=serializer.validated_data["ids"], model="lead")


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = EmployeeFilter
    filter_backends = (DjangoFilterBackend,)

    def get_serializer_class(self):
        if self.action in ["list", "create", "update"]:
            return EmployeeListSerializer
        return EmployeeDetailSerializer

    @action(detail=False, methods=["post"], url_path="export")
    def export_employee(self, request):
        serializer = ExportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return export_to_csv(ids=serializer.validated_data["ids"], model="employee")
