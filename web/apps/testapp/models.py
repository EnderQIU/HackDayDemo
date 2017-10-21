from django.db import models

# Create your models here.

class YoukuUser(models.Model):
    login_cookie = models.CharField(max_length=300)
