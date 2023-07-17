from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    created_date = models.DateTimeField(auto_now_add=True)
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')

    class Meta:
        ordering = ['-created_date']
        unique_together = ['owner', 'follower']

    def __str__(self):
        return f'{self.owner} {self.follower}'

