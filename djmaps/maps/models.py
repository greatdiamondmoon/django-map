from django.db import models

class Maps(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField()

