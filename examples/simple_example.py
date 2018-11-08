import asyncio
import sys
sys.path.insert(0, '../')
import r6sapi as api

@asyncio.coroutine
def run():
    auth = api.Auth("alex@ksso.net", "")
    
    player = yield from auth.get_player("zesquirrelnator", "uplay_test")
    operator = yield from player.get_operator("sledge")
    print(operator.kills)
    
asyncio.get_event_loop().run_until_complete(run())