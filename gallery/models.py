from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='gallery/')  # AWS S3 handles storage
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Image {self.id}"
