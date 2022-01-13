from typing import Optional

from dipdup.models import OperationData, Origination, Transaction
from dipdup.context import HandlerContext

import fxhash_indexer.models as models

from fxhash_indexer.types.gentk_minter_v1.parameter.mint import MintParameter
from fxhash_indexer.types.gentk_minter_v1.storage import GentkMinterV1Storage
from fxhash_indexer.types.gentk.parameter.mint import MintParameter
from fxhash_indexer.types.gentk.storage import GentkStorage
from utils import fromhex

async def on_mint_v1(
    ctx: HandlerContext,
    mint_minter: Transaction[MintParameter, GentkMinterV1Storage],
    mint: Transaction[MintParameter, GentkStorage],
) -> None:
    buyer, _ = await models.Holder.get_or_create(address=mint_minter.data.sender_address)
    gentk = await models.GENTK.get(id=mint.parameter.issuer_id)

    mint = models.Mint(
        iteration=mint.parameter.iteration,
        token_id=mint.parameter.token_id,
        issuer_id=mint_minter.parameter.issuer_id,
        buyer=buyer,
        gentk=gentk,
        amount=1,
        ophash=mint.data.hash,
        level=mint.data.level,
        timestamp=mint.data.timestamp,
        metadata=fromhex(mint.parameter.metadata[""])
    )
    await mint.save()

    token=models.Token(
        id=mint.token_id,
        mint=mint,
        gentk=gentk,
        buyer=buyer,
        amount=1,
        level=mint.level,
        timestamp=mint.timestamp,
        metadata=mint.metadata

    )

    gentk.mintable_amount -= 1  # type: ignore
    await gentk.save()
    await token.save()

    buyer, _ = await models.GENTKHolder.get_or_create(gentk=gentk, holder=buyer)
    buyer.quantity+=1
    await buyer.save()
