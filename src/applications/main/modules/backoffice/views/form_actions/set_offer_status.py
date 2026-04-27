from ....usecases import setOfferStatus
from .....models import Offer

def employee_action_set_offer_status(request, form_type):
    """EMPLOYEE ADMIN PANEL FORM ACTION TO (accept/decline) PROVIDER OFFER """
    if form_type == "offer_action":
        offer_id = request.POST.get("offer_id")
        
        offer = Offer.objects.get(id=offer_id)
        action = request.POST.get("action")
        
        if offer_id and action:
            setOfferStatus(offer, request.user, action)
