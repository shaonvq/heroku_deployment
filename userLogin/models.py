from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars',blank=True)
    steam = models.URLField(blank=True,verbose_name='Steam URL')

    def __str__(self):
        return self.user.username