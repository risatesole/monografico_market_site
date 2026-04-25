
# import logging
# from ...applications.main.models import Offer,  Batch
# logger = logging.getLogger(__name__)





# def tracer(func):
#     def wrapper(offer_id, status="PENDING"):
#         print(f"[TRACE] Calling {func.__name__}")
#         # ###########################################################
#         # offer = Offer.objects.select_related("product").get(id=offer_id)
#         product = offer.product
#         provider = offer.provider
#         acepted_by = None
#         unitperbatch = offer.unitperbatch
#         price = offer.priceperbatch
#         datetime = None
#         # print(f"{offer.provider}")
#         return func(offer_id,status)
#     return wrapper
















# # def tracer(func):
# #     def wrapper(*args, **kwargs):
# #         print(f"[TRACE] Calling {func.__name__}")
# #         print(f"  args: {args}")
# #         print(f"  kwargs: {kwargs}")
# #         return func(*args, **kwargs)
# #     return wrapper