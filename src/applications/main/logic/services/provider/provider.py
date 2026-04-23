from datetime import datetime
from ....models import Product, Offer

class ProviderService:
    def setOffer(self, providerid, productid, quantity, price):
        print(f"###########################################")
        print(f"Executing setOffer(): ")
        print(f"providerid: {providerid}")
        print(f"product: {productid}")
        print(f"quantity: {quantity}")
        print(f"price: {price}")
        print(f"###########################################")

        try:
            # 1. Retrieve the product instance
            product_instance = Product.objects.get(id=productid)

            # 2. Create and save the Offer
            new_offer = Offer.objects.create(
                product=product_instance,
                providerid=providerid,
                datetime= datetime.now(),
                priceperunit=price,
                unitquantity=quantity,
                status="PENDING"  
            )
            
            print(f"Successfully created Offer ID: {new_offer.id}")
            return new_offer

        except Product.DoesNotExist:
            print(f"Error: Product with ID {productid} not found.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
