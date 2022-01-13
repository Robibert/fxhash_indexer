
from dipdup.context import HandlerContext
from fxhash_indexer.types.user_registry.parameter.update_profile import UpdateProfileParameter
from fxhash_indexer.types.user_registry.storage import UserRegistryStorage
from dipdup.models import Transaction
import fxhash_indexer.models as models
from utils import fromhex

async def user_registry_on_update_profile(
    ctx: HandlerContext,
    update_profile: Transaction[UpdateProfileParameter, UserRegistryStorage],
) -> None:
    creator, _ = await models.Holder.get_or_create(address=update_profile.data.sender_address)
    creator.name=fromhex(update_profile.parameter.name)
    creator.metadata_file=fromhex(update_profile.parameter.metadata)

    await creator.save()