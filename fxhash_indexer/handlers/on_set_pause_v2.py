from fxhash_indexer.handlers.on_set_pause_v1 import on_set_pause_v1

async def on_set_pause_v2(*args,**kwargs):
    return await on_set_pause_v1(*args,**kwargs)