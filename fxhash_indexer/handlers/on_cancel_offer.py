from typing import Optional

from dipdup.models import OperationData, Origination, Transaction
from dipdup.context import HandlerContext

import fxhash_indexer.models as models

from fxhash_indexer.types.offer.parameter.cancel_offer import CancelOfferParameter
from fxhash_indexer.types.offer.storage import OfferStorage


async def on_cancel_offer(
    ctx: HandlerContext,
    cancel_offer: Transaction[CancelOfferParameter, OfferStorage],
) -> None:
    offer= await models.Offer.filter(id=cancel_offer.parameter.__root__).get_or_none()
    if offer is None:
        ctx.logger.warn("offer does not exist")
        return
    offer.status = models.OfferStatus.CANCELED
    offer.level=cancel_offer.data.level
    await offer.save()