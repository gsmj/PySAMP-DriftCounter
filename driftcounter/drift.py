from pysamp.event import event


class Drift:
    ...

    @event("OnPlayerDriftStart")
    def on_start(cls, player_id: int) -> None:
        return (Player(player_id), )

    @event("OnPlayerDriftUpdate")
    def on_update(cls, player_id: int, value: int, combo: int, flag_id: int, distance: float, speed: float) -> None:
        return (Player(player_id), value, combo, flag_id, distance, speed)

    @event("OnPlayerDriftEnd")
    def on_end(cls, player_id: int, value: int, combo: int, reason: int):
        return (Player(player_id), value, combo, reason)

from pysamp.player import Player # noqa
