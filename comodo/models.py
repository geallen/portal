from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User,BaseUserManager,AbstractBaseUser
from django.conf import settings

# Create your models here.

#
# class PortalUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     username = models.TextField()
#     phone_number = models.TextField()
#     address = models.TextField()
#
#     def __unicode__(self):
#         return self.user.first_name
#
#     def __str__(self):
#         return self.user.first_name

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=255,verbose_name='username')
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


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
