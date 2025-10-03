from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
     bio = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name='بیوگرافی' 
        )
     profile_picture = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True,
        verbose_name='عکس پروفایل'
        )
     class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        
     def __str__(self):
        return self.username
     
