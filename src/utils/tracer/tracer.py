
import logging
from ...applications.main.models import Offer 
logger = logging.getLogger(__name__)


def getOfferDetails(offerid):
    offer = Offer.objects.select_related("product").get(id=offerid)
    logger.info(offer.product.name)
    # print(offer.product.name)


def tracer(func):
    def wrapper(offer_id, status="PENDING"):
        print(f"[TRACE] Calling {func.__name__}")



        # ###########################################################
        offer = Offer.objects.select_related("product").get(id=offer_id)
        product = offer.product

        print(f"{product.name}")
        return func(offer_id,status)
    return wrapper
















# def tracer(func):
#     def wrapper(*args, **kwargs):
#         print(f"[TRACE] Calling {func.__name__}")
#         print(f"  args: {args}")
#         print(f"  kwargs: {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper