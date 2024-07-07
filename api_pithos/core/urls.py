from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from api_pithos.core.api.views import LeadDocumentViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()


router.register("leads", LeadDocumentViewSet, basename="lead")

app_name = "core"
urlpatterns = router.urls
