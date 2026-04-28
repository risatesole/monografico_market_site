# todo: relocate this method to product module
from ..services.provider import ProviderService
def get_all_product_sale_requests():
    provider_service = ProviderService()
    return provider_service.getAllOffers()
