from typing import Optional

from dipdup.models import OperationData, Origination, Transaction
from dipdup.context import HandlerContext

import fxhash_indexer.models as models

from fxhash_indexer.types.offer.parameter.offer import OfferParameter
from fxhash_indexer.types.offer.storage import OfferStorage


async def on_offer(
    ctx: HandlerContext,
    offer: Transaction[OfferParameter, OfferStorage],
) -> None:
    holder, _ = await models.Holder.get_or_create(address=offer.data.sender_address)
    mint=await models.Mint.get(token_id=offer.parameter.objkt_id)
    gentk = await models.GENTK.get(id=mint.issuer_id)
    offer_id = int(offer.storage.counter) - 1

    is_valid=offer.parameter.creator == gentk.creator_id and int(offer.parameter.royalties) == int(gentk.royalties)
    
    offer = models.Offer(
        id=offer_id,  # type: ignore
        creator=holder,
        gentk=gentk,
        mint=mint,
        price=offer.parameter.price,
        amount=1,
        amount_left=1,
        status=models.OfferStatus.ACTIVE,
        ophash=offer.data.hash,
        level=offer.data.level,
        timestamp=offer.data.timestamp,
        royalties=offer.parameter.royalties,
        is_valid=is_valid,
    )

    await offer.save()
