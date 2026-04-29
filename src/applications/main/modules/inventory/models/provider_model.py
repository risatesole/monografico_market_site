from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
