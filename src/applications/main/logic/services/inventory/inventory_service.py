from ....models import Batch, User 
class InventoryService():
    def create_batch(self,product,provider: User,accepted_by: User,unitperbatch,acquisition_price,datetime):
        batch = Batch.objects.create(
            product = product,
            provider = provider,
            accepted_by = accepted_by,
            unitperbatch = unitperbatch,
            acquisition_price = acquisition_price,
            datetime = datetime
        )
        return batch
