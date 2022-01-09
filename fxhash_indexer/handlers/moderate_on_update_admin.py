
from dipdup.models import Transaction
from fxhash_indexer.types.moderation.parameter.update_admin import UpdateAdminParameter
from dipdup.context import HandlerContext
from fxhash_indexer.types.moderation.storage import ModerationStorage
import fxhash_indexer.models as models

async def moderate_on_update_admin(
    ctx: HandlerContext,
    update_admin: Transaction[UpdateAdminParameter, ModerationStorage],
) -> None:
    address=update_admin.parameter.__root__
    admin, _ = await models.Holder.get_or_create(address=address)
    admin.is_moderation_admin=True
    await admin.save()

    old_admin=await models.Holder.filter(is_moderation_admin=True).get_or_none()
    if old_admin is not None:
        old_admin.is_moderation_admin=False
        await old_admin.save()