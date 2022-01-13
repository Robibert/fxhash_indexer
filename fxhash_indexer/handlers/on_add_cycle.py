
from datetime import timedelta
from dipdup.context import HandlerContext
import fxhash_indexer.models as models


from fxhash_indexer.types.cycle_adder.storage import CycleAdderStorage
from dipdup.models import Transaction
from fxhash_indexer.types.cycle_adder.parameter.add_cycle import AddCycleParameter

async def on_add_cycle(
    ctx: HandlerContext,
    add_cycle: Transaction[AddCycleParameter, CycleAdderStorage],
) -> None:
    
    
    last_cycles=await models.Cycle.all().order_by("-id").limit(1).all()
    if not last_cycles:
        id=0
    else:
        id=max([s.id for s in last_cycles])+1
    
    cycle=models.Cycle(id=id)
    cycle.closing_duration=timedelta(seconds=int(add_cycle.parameter.closing_duration))
    cycle.opening_duration=timedelta(seconds=int(add_cycle.parameter.opening_duration))
    cycle.start=add_cycle.data.timestamp
    cycle.level=add_cycle.data.level
    cycle.timestamp=add_cycle.data.timestamp

    await cycle.save()