from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='blog_iamges/',blank=True)

    def __str__(self):
        return self.title
