from rest_framework import routers

from .views import (
    ArtifactAnnotationViewSet,
    ArtifactStarsViewSet,
    ArtifactViewSet,
    ProductClientViewSet,
    ProductDevicesVersionHistoryViewSet,
)

router = routers.DefaultRouter()
router.register(r'artifacts', ArtifactViewSet)
router.register(r'artifact_annotations', ArtifactAnnotationViewSet)
router.register(r'artifact_stars', ArtifactStarsViewSet)
router.register(r'product_clients', ProductClientViewSet)
router.register(r'product_devices_version_history', ProductDevicesVersionHistoryViewSet)

urlpatterns = router.urls
