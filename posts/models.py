from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Post(models.Model):
    class Meta(object):
        db_table = "post"

    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )
    body = models.CharField(
        'Body', blank=False, null=False, max_length=140, db_index=True
    )
    created_at = models.DateTimeField(
        'Created Dateline', blank=True, auto_now_add=True
    )
    likes = models.ManyToManyField(
        User, related_name='likes', default=0
    )
    image = CloudinaryField(
        'image', blank=True, db_index=True
    )

    def total_likes(self):
        return self.likes.count()
