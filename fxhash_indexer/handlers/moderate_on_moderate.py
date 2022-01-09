
from dipdup.models import Transaction
from fxhash_indexer.types.moderation.parameter.moderate import ModerateParameter
from dipdup.context import HandlerContext
from fxhash_indexer.types.moderation.storage import ModerationStorage
import fxhash_indexer.models as models

async def moderate_on_moderate(
    ctx: HandlerContext,
    moderate: Transaction[ModerateParameter, ModerationStorage],
) -> None:
    address=moderate.parameter.address
    user, _ = await models.Holder.get_or_create(address=address)
    user.moderation_state=moderate.parameter.state
    await user.save()