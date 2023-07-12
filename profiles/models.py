from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_image = models.ImageField(upload_to='snapit/', default='user')

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.owner}'


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
