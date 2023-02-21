from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import (
    Artifact,
    ArtifactAnnotation,
    ArtifactStars,
    ProductClient,
    ProductDevicesVersionHistory,
)
from .serializers import (
    ArtifactAnnotationSerializer,
    ArtifactSerializer,
    ArtifactStarsSerializer,
    ProductClientSerializer,
    ProductDevicesVersionHistorySerializer,
)


class ArtifactViewSet(viewsets.ModelViewSet):
    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer
    filter_backends = [DjangoFilterBackend]


class ArtifactAnnotationViewSet(viewsets.ModelViewSet):
    queryset = ArtifactAnnotation.objects.all()
    serializer_class = ArtifactAnnotationSerializer
    filter_backends = [DjangoFilterBackend]


class ArtifactStarsViewSet(viewsets.ModelViewSet):
    queryset = ArtifactStars.objects.all()
    serializer_class = ArtifactStarsSerializer
    filter_backends = [DjangoFilterBackend]


class ProductClientViewSet(viewsets.ModelViewSet):
    queryset = ProductClient.objects.all()
    serializer_class = ProductClientSerializer
    filter_backends = [DjangoFilterBackend]


class ProductDevicesVersionHistoryViewSet(viewsets.ModelViewSet):
    queryset = ProductDevicesVersionHistory.objects.all()
    serializer_class = ProductDevicesVersionHistorySerializer
    filter_backends = [DjangoFilterBackend]
