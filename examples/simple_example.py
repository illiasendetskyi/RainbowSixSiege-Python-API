import asyncio
import sys
sys.path.insert(0, '../')
import r6sapi as api

@asyncio.coroutine
def run():
    auth = api.Auth("alex@ksso.net", "password")
    player = yield from auth.get_player("MrQW3RTY666", "uplay_test")
    stats = yield from player.check_general()
    print(f"Matches played for MrQW3RTY666 on test servers (was 48): {player.matches_played}")
    player = yield from auth.get_player("Griefdrums.", "uplay")
    stats = yield from player.check_general()
    print(f"Matches played for Griefdrums. on test servers (was 998): {player.matches_played}")
    yield from auth.session.close() #nicely close the session


    
asyncio.get_event_loop().run_until_complete(run())