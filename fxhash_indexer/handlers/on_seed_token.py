
from dipdup.models import Transaction
from fxhash_indexer.types.gentk_minter_v2.storage import GentkMinterV2Storage
from dipdup.context import HandlerContext
from fxhash_indexer.types.gentk_minter_v2.parameter.seed_token import SeedTokenParameter

async def on_seed_token(
    ctx: HandlerContext,
    seed_token: Transaction[SeedTokenParameter, GentkMinterV2Storage],
) -> None:
    pass