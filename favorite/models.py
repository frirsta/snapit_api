from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Favorite(models.Model):
    """
    Save post model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='favorite')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f"{self.owner} by {self.post}"