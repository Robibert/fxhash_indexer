from fxhash_indexer.handlers.on_update_issuer_v1 import on_update_issuer_v1

async def on_update_issuer_v2(*args,**kwargs):
    return await on_update_issuer_v1(*args,**kwargs)