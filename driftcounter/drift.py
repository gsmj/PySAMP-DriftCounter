from pysamp.event import event


@event("OnPlayerDriftStart")
def on_start(player_id: int):
    return (Player(player_id), )


@event("OnPlayerDriftUpdate")
def on_update(player_id: int, value: int, combo: int, flag_id: int, distance: float, speed: float):
    return (Player(player_id), value, combo, flag_id, distance, speed)


@event("OnPlayerDriftEnd")
def on_end(player_id: int, value: int, combo: int, reason: int):
    return (Player(player_id), value, combo, reason)

from pysamp.player import Player # noqa
