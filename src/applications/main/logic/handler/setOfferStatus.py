from ..services.provider import ProviderService

def setOfferStatus(offer_id, status="PENDING"):
    providerService = ProviderService()

    if status == "ACCEPTED":
        providerService.setOfferStatusACCEPTED(offer_id)
    elif status == "DECLINED":
        providerService.setOfferStatusDECLINED(offer_id)
