from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video


class Video(models.Model):
    """
    Video model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    caption = models.TextField(max_length=250)
    video = models.FileField(upload_to='snapit/', storage=VideoMediaCloudinaryStorage(),
                             validators=[validate_video])
    file = models.ImageField(
        upload_to='snapit/', blank=True, storage=RawMediaCloudinaryStorage())

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f'{self.id} {self.caption}'
