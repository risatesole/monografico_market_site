from datetime import datetime
from ....models import Product, Offer

class ProviderService:
    def setOffer(self, product, provider, priceperbatch, batchquantity,unitperbatch):
        try:
            product_instance = Product.objects.get(id=product)
            offer = Offer.objects.create(
                product = product_instance,
                provider = provider,
                datetime = datetime.now(),
                priceperbatch = priceperbatch,
                batchquantity = batchquantity,
                unitperbatch = unitperbatch,
                status = "PENDING"
            )

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
                offers = offers.filter(provider=providerid)

            if status is not None:
                offers = offers.filter(status=status)

            # Order by newest first (optional but useful)
            offers = offers.order_by("-datetime")

            return offers

        except Exception as e:
            print(f"Error retrieving offers: {e}")
            return Offer.objects.none()
   
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
