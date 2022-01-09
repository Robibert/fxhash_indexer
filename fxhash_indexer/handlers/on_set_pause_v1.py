from typing import Optional

from dipdup.models import OperationData, Origination, Transaction
from dipdup.context import HandlerContext

import fxhash_indexer.models as models

from fxhash_indexer.types.gentk_minter.parameter.set_pause import SetPauseParameter
from fxhash_indexer.types.gentk_minter.storage import GentkMinterStorage


async def on_set_pause_v1(
    ctx: HandlerContext,
    set_pause: Transaction[SetPauseParameter, GentkMinterStorage],
) -> None:
    status,_=await models.MintStatus.get_or_create(id=0)
    pause=set_pause.parameter.__root__
    status.pause=pause
    status.level=set_pause.data.level
    status.timestamp=set_pause.data.timestamp
    status.ophash=set_pause.data.hash
    await status.save()