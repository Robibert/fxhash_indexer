
from fxhash_indexer.types.gentk.parameter.transfer import TransferParameter
from dipdup.context import HandlerContext
from fxhash_indexer.types.gentk.storage import GentkStorage
from dipdup.models import Transaction
import fxhash_indexer.models as models

async def on_transfer(
    ctx: HandlerContext,
    transfer: Transaction[TransferParameter, GentkStorage],
) -> None:
    for t in transfer.parameter.__root__:
        sender, _ = await models.Holder.get_or_create(address=t.from_)
        for tx in t.txs:
            if int(tx.amount)==0:
                continue
            if int(tx.amount)!=1:
                raise ValueError()

            mint=await models.Mint.get(token_id=tx.token_id)
            gentk = await models.GENTK.get(id=mint.gentk_id)
            token=await models.Token.get(id=tx.token_id)

            
            receiver, _ = await models.Holder.get_or_create(address=tx.to_)
            sender_holding, _ = await models.GENTKHolder.get_or_create(gentk=gentk, holder=sender)
            receiver_holding, _ = await models.GENTKHolder.get_or_create(gentk=gentk, holder=receiver)

            sender_holding.quantity -= int(tx.amount)  # type: ignore
            receiver_holding.quantity += int(tx.amount)  # type: ignore
            
            token.buyer=receiver

            await sender_holding.save()
            await receiver_holding.save()
            await token.save()

            if tx.to_ == 'tz1burnburnburnburnburnburnburjAYjjX':
                gentk.supply -= int(tx.amount)  # type: ignore
                await gentk.save()
            pass
