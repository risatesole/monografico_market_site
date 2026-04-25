from ..services.provider import ProviderService
from ..services.inventory import InventoryService
from ...models import Offer
from ...models import User
from ...models import Product
from datetime import datetime

def setOfferStatus(offer: Offer, action_user: User, status="PENDING"):
    print(f"debug: ")
    print(f"product = {offer.product.name}")
    providerService = ProviderService()
    inventoryService = InventoryService()
    current_time = datetime.now()

    if status == "ACCEPTED":
        providerService.setOfferStatusACCEPTED(offer)
        product = offer.product
        provider = offer.provider
        accepted_by = action_user 
        unitperbatch = offer.unitperbatch
        acquisition_price = offer.priceperbatch
        Datetime = current_time

        inventoryService.create_batch(product,provider,accepted_by,unitperbatch,acquisition_price,Datetime)

    elif status == "DECLINED":
        providerService.setOfferStatusDECLINED(offer)
