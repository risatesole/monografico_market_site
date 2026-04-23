from django.db import models
from ...models import User

class provider_request(models.Model):
    """
    this model represents when a user a request to the provider with text that the user wants to be a provider
    
    """
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("vetting", "Vetting"),
        ("approved", "Approved"),
    ]
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    external_id = models.CharField(max_length=255)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application {self.id}"
