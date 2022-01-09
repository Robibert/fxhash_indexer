
from fxhash_indexer.types.moderation.parameter.ban import BanParameter
from dipdup.models import Transaction
from dipdup.context import HandlerContext
from fxhash_indexer.types.moderation.storage import ModerationStorage
import fxhash_indexer.models as models


async def moderate_on_ban(
    ctx: HandlerContext,
    ban: Transaction[BanParameter, ModerationStorage],
) -> None:
    address=ban.parameter.__root__
    banned, _ = await models.Holder.get_or_create(address=address)
    banned.is_banned=True
    await banned.save()