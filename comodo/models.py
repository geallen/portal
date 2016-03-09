from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class PortalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.TextField()
    address = models.TextField()

    def __unicode__(self):
        return self.user.first_name

    def __str__(self):
        return self.user.first_name


class Post(models.Model):
    title = models.CharField(max_length=120)
    message = models.TextField()
    release_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    unpublishing_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_accomplished = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class PostConfirmation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.user.name

    def __str__(self):
        return self.user.name
