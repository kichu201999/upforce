from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):


    class Meta:
        db_table = "user"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.username


class BlogPost(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    discription = models.TextField(null=True, blank=True)
    content = models.CharField(max_length=256, null=True, blank=True)
    user = models.ForeignKey(
        User, related_name="blog",
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    class Meta:
        db_table = "blog_post"


class Like(models.Model):
    liked_user = models.ForeignKey(
        User, related_name='likes',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    post = models.ForeignKey(
        BlogPost, related_name='likes',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
