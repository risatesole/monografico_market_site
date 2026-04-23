from django.db import models
from .model_batch import Batch

class Unit(models.Model):
    batch_id = models.ForeignKey(
        Batch,
        on_delete=models.CASCADE
    )
    