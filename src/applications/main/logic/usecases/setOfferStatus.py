from ..services.provider import ProviderService
# from .....utils.tracer.tracer import tracer

# @tracer
def setOfferStatus(offer_id, status="PENDING"):
    providerService = ProviderService()

    if status == "ACCEPTED":
        providerService.setOfferStatusACCEPTED(offer_id)
    elif status == "DECLINED":
        providerService.setOfferStatusDECLINED(offer_id)
