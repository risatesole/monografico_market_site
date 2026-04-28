# todo: delete method

from ..services.provider import ProviderService

def submit_product_sale_request(product, provider, priceperbatch, batchquantity,unitperbatch):
    """Submit a provider's request to sell a product for later approval or rejection."""
    provider_service = ProviderService()
    provider_service.setOffer(product, provider, priceperbatch, batchquantity,unitperbatch)

