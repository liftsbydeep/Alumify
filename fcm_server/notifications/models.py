from django.db import models

class User(models.Model):
    uuid = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    fcm_token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
