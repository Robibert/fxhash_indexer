from typing import Optional

from dipdup.models import OperationData, Origination, Transaction
from dipdup.context import HandlerContext

import fxhash_indexer.models as models

from fxhash_indexer.types.offer.parameter.update_enabled import UpdateEnabledParameter
from fxhash_indexer.types.offer.storage import OfferStorage


async def on_update_enabled(
    ctx: HandlerContext,
    update_enabled: Transaction[UpdateEnabledParameter, OfferStorage],
) -> None:
    status,_=await models.MintStatus.get_or_create(id=0)
    enabled=update_enabled.parameter.__root__
    status.enabled=enabled
    status.level=update_enabled.data.level
    status.timestamp=update_enabled.data.timestamp
    status.ophash=update_enabled.data.hash
    await status.save()