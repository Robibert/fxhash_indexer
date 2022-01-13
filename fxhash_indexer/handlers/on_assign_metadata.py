
from dipdup.models import Transaction
from dipdup.context import HandlerContext
from fxhash_indexer.types.gentk.storage import GentkStorage
from fxhash_indexer.types.gentk.parameter.assign_metadata import AssignMetadataParameter
import fxhash_indexer.models as models
from utils import fromhex

async def on_assign_metadata(
    ctx: HandlerContext,
    assign_metadata: Transaction[AssignMetadataParameter, GentkStorage],
) -> None:
    token=await models.Token.filter(id=assign_metadata.parameter.token_id).get()
    mint=await token.mint

    token.metadata=fromhex(assign_metadata.parameter.metadata[""])
    mint.metadata=fromhex(assign_metadata.parameter.metadata[""])

    await token.save()
    await mint.save()