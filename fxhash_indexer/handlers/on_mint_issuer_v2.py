from typing import Optional

from dipdup.models import  Transaction
from dipdup.context import HandlerContext

import fxhash_indexer.models as models

from fxhash_indexer.types.gentk_minter_v2.parameter.mint_issuer import MintIssuerParameter
from fxhash_indexer.types.gentk_minter_v2.storage import GentkMinterV2Storage
from utils import fromhex

async def on_mint_issuer_v2(
        ctx: HandlerContext,
        mint_issuer: Transaction[MintIssuerParameter, GentkMinterV2Storage],
    ) -> None:
    creator, _ = await models.Holder.get_or_create(address=mint_issuer.data.sender_address)

    gentk_id=int(mint_issuer.data.diffs[0]["content"]["value"]["last_issuer_minted"])
    if await models.GENTK.exists(id=gentk_id):
        return

    metadata = ''
    if mint_issuer.parameter.metadata:
        metadata = fromhex(mint_issuer.parameter.metadata)

    gentk = models.GENTK(
        id=gentk_id,
        royalties=mint_issuer.parameter.royalties,
        title='',
        description='',
        artifact_uri='',
        display_uri='',
        thumbnail_uri='',
        metadata=metadata,
        mime='',
        creator=creator,
        supply=mint_issuer.parameter.amount,
        level=mint_issuer.data.level,
        timestamp=mint_issuer.data.timestamp,

        contract_version=2,
        
        mintable_amount=mint_issuer.parameter.amount,
        mint_price=mint_issuer.parameter.price,
        mint_enabled=mint_issuer.parameter.enabled,
    )
    await gentk.save()


