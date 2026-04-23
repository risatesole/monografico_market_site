from ..services.provider import ProviderService

def submit_product_sale_request(providerid,productid,quantity,price):
    """Submit a provider's request to sell a product for later approval or rejection."""
    provider_service = ProviderService()
    provider_service.setRequestSellProduct(providerid,productid,quantity,price)

