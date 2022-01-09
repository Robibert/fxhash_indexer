
from fxhash_indexer.types.moderation.parameter.verify import VerifyParameter
from dipdup.models import Transaction
from dipdup.context import HandlerContext
from fxhash_indexer.types.moderation.storage import ModerationStorage
import fxhash_indexer.models as models

async def moderate_on_verify(
    ctx: HandlerContext,
    verify: Transaction[VerifyParameter, ModerationStorage],
) -> None:
    address=verify.parameter.__root__
    verified, _ = await models.Holder.get_or_create(address=address)
    verified.is_verified=True
    await verified.save()