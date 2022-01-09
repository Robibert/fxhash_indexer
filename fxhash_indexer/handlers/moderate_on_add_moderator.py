
from fxhash_indexer.types.moderation.storage import ModerationStorage
from dipdup.models import Transaction
from dipdup.context import HandlerContext
from fxhash_indexer.types.moderation.parameter.add_moderator import AddModeratorParameter
import fxhash_indexer.models as models

async def moderate_on_add_moderator(
    ctx: HandlerContext,
    add_moderator: Transaction[AddModeratorParameter, ModerationStorage],
) -> None:
        address=add_moderator.parameter.__root__
        moderator, _ = await models.Holder.get_or_create(address=address)
        moderator.is_moderator=True
        await moderator.save()
