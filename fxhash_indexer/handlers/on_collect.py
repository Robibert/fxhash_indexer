from typing import Optional

from dipdup.models import OperationData, Origination, Transaction
from dipdup.context import HandlerContext

import fxhash_indexer.models as models

from fxhash_indexer.types.offer.parameter.collect import CollectParameter
from fxhash_indexer.types.offer.storage import OfferStorage


async def on_collect(
    ctx: HandlerContext,
    collect: Transaction[CollectParameter, OfferStorage],
) -> None:
    offer = await models.Offer.get(id=collect.parameter.__root__)
    seller = await offer.creator
    buyer, _ = await models.Holder.get_or_create(address=collect.data.sender_address)
    gentk_id=offer.gentk_id

    trade = models.Trade(
        offer=offer,
        seller=seller,
        buyer=buyer,
        gentk_id=gentk_id,
        amount=1,
        ophash=collect.data.hash,
        level=collect.data.level,
        timestamp=collect.data.timestamp,
    )

    offer.amount_left -= 1  # type: ignore
    if offer.amount_left == 0:
        offer.status = models.OfferStatus.FINISHED
    
    await offer.save()
    await trade.save()