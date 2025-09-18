from storages.backends.s3boto3 import S3Boto3Storage
from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(
        upload_to='gallery/',
        storage=S3Boto3Storage()
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Image {self.id}"
