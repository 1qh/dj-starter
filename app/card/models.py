from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Artifact(models.Model):
    video_path = models.CharField(max_length=255)
    product_device_version = models.CharField(max_length=255)


class ArtifactAnnotation(models.Model):
    artifact = models.ForeignKey(Artifact, on_delete=models.CASCADE)
    is_abnormal = models.BooleanField()
    comment = models.CharField(max_length=255)
    annotator = models.ForeignKey(User, on_delete=models.CASCADE)


class ArtifactStars(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artifact = models.ForeignKey(Artifact, on_delete=models.CASCADE)


class ProductClient(models.Model):
    name = models.CharField(max_length=255)


class ProductDevicesVersionHistory(models.Model):
    client = models.ForeignKey(ProductClient, on_delete=models.CASCADE)
    version = models.CharField(max_length=255)
