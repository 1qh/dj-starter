from django.contrib import admin

from .models import (
    Artifact,
    ArtifactAnnotation,
    ArtifactStars,
    ProductClient,
    ProductDevicesVersionHistory,
)

admin.site.register(
    [
        Artifact,
        ArtifactAnnotation,
        ArtifactStars,
        ProductClient,
        ProductDevicesVersionHistory,
    ]
)
