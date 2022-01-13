
import fxhash_indexer.models as models

from fxhash_indexer.types.cycle_updater.parameter.update_cycles import UpdateCyclesParameter
from dipdup.context import HandlerContext
from fxhash_indexer.types.cycle_updater.storage import CycleUpdaterStorage
from dipdup.models import Transaction

async def on_update_cycles(
    ctx: HandlerContext,
    update_cycles: Transaction[UpdateCyclesParameter, CycleUpdaterStorage],
) -> None:

    for cycle in await models.Cycle.filter(is_enforced=True).all():
        cycle.is_enforced=False
        await cycle.save()
    
    id=int(update_cycles.parameter.__root__[0])
    cycle= await models.Cycle.filter(id=id).get()
    cycle.is_enforced=True
    
    await cycle.save()