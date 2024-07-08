from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from api_pithos.core.api.views import EmployeeViewSet
from api_pithos.core.api.views import LeadDocumentViewSet
from api_pithos.core.api.views import LeadViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()


router.register("leads", LeadViewSet, basename="lead")
router.register("employees", EmployeeViewSet, basename="employee")

# Elasticsearch
router.register("lead-search", LeadDocumentViewSet, basename="leaddocument")

app_name = "core"
urlpatterns = router.urls
