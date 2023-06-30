from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    post model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    caption = models.TextField(max_length=250)
    image = models.ImageField(upload_to='snapit/')

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f'{self.id} {self.caption}'

