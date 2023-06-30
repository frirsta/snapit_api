from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from cloudinary.models import CloudinaryField

class Post(models.Model):
    """
    post model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    caption = models.TextField(max_length=250)
    image = CloudinaryField('image')
    video = CloudinaryField('video')
    file = models.ImageField(upload_to='snapit/', blank=True, storage=RawMediaCloudinaryStorage())

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f'{self.id} {self.caption}'

