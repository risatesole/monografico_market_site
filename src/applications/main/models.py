from .modules.models.model_user import User  as User
from .modules.models.model_user import UserRoles as UserRoles
from .modules.models.model_product import Product as Product 
from .modules.models.model_offer import Offer as Offer
from .modules.product.models.price_model import Price as Price # todo: remove from here and use only in usecase call to product module

from django.db import models
from django.utils import timezone

class Batch(models.Model):
    class Meta:
        db_table = "batch"
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    provider = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="provided_batches",
        limit_choices_to={"role": UserRoles.CUSTOMER} # TODO: make this provider
    )

    accepted_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="accepted_batches",
        limit_choices_to={"role": UserRoles.CUSTOMER} # TODO: make this employee
    )
    unitperbatch = models.IntegerField()
    acquisition_price = models.FloatField()
    datetime = models.DateTimeField(null=True, blank=True)
