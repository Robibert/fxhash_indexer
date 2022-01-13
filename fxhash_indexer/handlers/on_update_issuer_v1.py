from typing import Optional

from dipdup.models import OperationData, Origination, Transaction
from dipdup.context import HandlerContext

import fxhash_indexer.models as models

from fxhash_indexer.types.gentk_minter_v1.parameter.update_issuer import UpdateIssuerParameter
from fxhash_indexer.types.gentk_minter_v1.storage import GentkMinterV1Storage


async def on_update_issuer_v1(
    ctx: HandlerContext,
    update_issuer: Transaction[UpdateIssuerParameter, GentkMinterV1Storage],
) -> None:
    gentk=await models.GENTK.get(id=update_issuer.parameter.issuer_id)
    gentk.mint_price=update_issuer.parameter.price
    gentk.royalties=update_issuer.parameter.royalties
    gentk.mint_enabled=update_issuer.parameter.enabled
    gentk.level=update_issuer.data.level
    gentk.timestamp=update_issuer.data.timestamp
    
    await gentk.save()