
from dipdup.models import Transaction
from fxhash_indexer.types.gentk_minter_v2.storage import GentkMinterV2Storage
from dipdup.context import HandlerContext
from fxhash_indexer.types.gentk_minter_v2.parameter.set_lock_time import SetLockTimeParameter

async def on_set_lock_time(
    ctx: HandlerContext,
    set_lock_time: Transaction[SetLockTimeParameter, GentkMinterV2Storage],
) -> None:
    pass