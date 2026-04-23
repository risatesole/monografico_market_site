from ..services.provider import ProviderService
def get_product_sale_requests(providerid):
    provider_service = ProviderService()
    return provider_service.getOffers(providerid)
