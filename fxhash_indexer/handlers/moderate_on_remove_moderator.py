import fxhash_indexer.models as models

from fxhash_indexer.types.moderation.parameter.remove_moderator import RemoveModeratorParameter
from dipdup.models import Transaction
from dipdup.context import HandlerContext
from fxhash_indexer.types.moderation.storage import ModerationStorage

async def moderate_on_remove_moderator(
    ctx: HandlerContext,
    remove_moderator: Transaction[RemoveModeratorParameter, ModerationStorage],
) -> None:
    address=remove_moderator.parameter.__root__
    moderator, _ = await models.Holder.get_or_create(address=address)
    moderator.is_moderator=False
    await moderator.save()
