from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='profile')
    profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True, default='/no_image-1')
    cover_photo = models.ImageField(upload_to='users/cover_photos', blank=True, null=True, default='/no_image-1')
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="profiles")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="update_profile")
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.email} {self.user.username}'