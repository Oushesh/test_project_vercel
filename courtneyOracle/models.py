from django.db import models
from datetime import datetime
from uuid import uuid4
from django.urls import reverse

# Create your models here.
def get_upload_path(instance, filename):
    """Return timestamp filename for user uploaded files."""

    ext = filename.split(".")[-1]
    time_stamp = datetime.today().strftime("%Y%m%d_%H%M%S")
    folder = datetime.today().strftime("%Y/%m")
    image_path = f"{folder}/{time_stamp}.{ext}"
    return image_path


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='blog_iamges/',blank=True)

    def __str__(self):
        return self.title


class UserActivity(models.Model):
    """
    A class representing user activity

    Uploading image to remove its background and downloading.
    """
    image = models.ImageField(upload_to=get_upload_path)
    result = models.ImageField(upload_to=get_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default=uuid4)

    class Meta:
        verbose_name = "User Activity"
        verbose_name_plural = "User Activities"

    def __str__(self) -> str:
        return str(self.slug)

    def get_absolute_url(self):
        return reverse("courtneyOracle:result", args=(self.slug,))
