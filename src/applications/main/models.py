from .logic.models.model_user import User  as User
from .logic.models.model_user import UserRoles as UserRoles
from .logic.models.model_product import Product as Product 
from .logic.models.model_offer import Offer as Offer

from django.db import models


class Batch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    provider = models.IntegerField() # TODO: make this a provider foreign key
    accepted_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"role": UserRoles.CUSTOMER} # TODO: make this employee
    )
    unitperbatch = models.IntegerField()
    price = models.FloatField()
    datetime = models.DateTimeField(null=True, blank=True)