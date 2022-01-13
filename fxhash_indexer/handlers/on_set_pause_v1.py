from typing import Optional

from dipdup.models import OperationData, Origination, Transaction
from dipdup.context import HandlerContext

import fxhash_indexer.models as models

from fxhash_indexer.types.gentk_minter_v1.parameter.set_pause import SetPauseParameter
from fxhash_indexer.types.gentk_minter_v1.storage import GentkMinterV1Storage


async def on_set_pause_v1(
    ctx: HandlerContext,
    set_pause: Transaction[SetPauseParameter, GentkMinterV1Storage],
) -> None:
    last_statuses=await models.MintStatus.all().order_by("-id").limit(1).all()
    if not last_statuses:
        id=0
    else:
        id=max([s.id for s in last_statuses])+1
    
    status,_=await models.MintStatus.get_or_create(id=id)
    pause=set_pause.parameter.__root__
    status.pause=pause
    status.level=set_pause.data.level
    status.timestamp=set_pause.data.timestamp
    status.ophash=set_pause.data.hash
    await status.save()