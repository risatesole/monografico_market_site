from datetime import datetime
from ....models import Product, Offer

class ProviderService:
    def setOffer(self, product, providerid, priceperbatch, batchquantity,unitperbatch):
        try:
            # 1. Retrieve the product instance
            product_instance = Product.objects.get(id=product)


            # print(f"Debug: ")
            # print(f"product = {product}")
            # print(f"providerid = {providerid}")
            # print(f"datetime = {datetime.now()}") # should be set automatically
            # print(f"priceperbatch = {priceperbatch}")
            # print(f"batchquantity = {batchquantity}")
            # print(f"unitperbatch: {unitperbatch}")
            # print(f"status should be set to pending here") # set status to pending

            offer = Offer.objects.create(
                product = product_instance,
                provider = providerid,
                datetime = datetime.now(),
                priceperbatch = priceperbatch,
                batchquantity = batchquantity,
                unitperbatch = unitperbatch,
                status = "PENDING"
            )

            # # 2. Create and save the Offer
            # new_offer = Offer.objects.create(
            #     product=product_instance,
            #     providerid=providerid,
            #     datetime= datetime.now(),
            #     priceperunit=price,
            #     unitquantity=quantity,
            #     status="PENDING"  
            # )
            
            # print(f"Successfully created Offer ID: {new_offer.id}")
            # return new_offer

        except Product.DoesNotExist:
            print(f"Error: Product with ID {product} not found.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def getOffers(self, providerid=None, status=None):
        try:
            offers = Offer.objects.all()

            # Optional filters
            if providerid is not None:
                offers = offers.filter(providerid=providerid)

            if status is not None:
                offers = offers.filter(status=status)

            # Order by newest first (optional but useful)
            offers = offers.order_by("-datetime")

            return offers

        except Exception as e:
            print(f"Error retrieving offers: {e}")
            return None
   
    def getAllOffers(self):
        try:
            return Offer.objects.all().order_by("-datetime")
        except Exception as e:
            print(f"Error retrieving all offers: {e}")
            return None

    def setOfferStatusACCEPTED(self, orderid):
        try:
            offer = Offer.objects.get(id=orderid)
            offer.status = "ACCEPTED"
            offer.save()

            return offer
        except Offer.DoesNotExist:
            print(f"Error: Offer with ID {orderid} not found.")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    def setOfferStatusDECLINED(self, offerid):
        try:
            offer = Offer.objects.get(id=offerid)
            offer.status = "DECLINED"
            offer.save()
            return offer
        except Offer.DoesNotExist:
            print(f"Error: Offer with ID {offerid} not found.")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
