from rest_framework import serializers

from .models import (
    Artifact,
    ArtifactAnnotation,
    ArtifactStars,
    ProductClient,
    ProductDevicesVersionHistory,
)


class ArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = '__all__'


class ArtifactAnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtifactAnnotation
        fields = '__all__'


class ArtifactStarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtifactStars
        fields = '__all__'


class ProductClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductClient
        fields = '__all__'


class ProductDevicesVersionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDevicesVersionHistory
        fields = '__all__'
