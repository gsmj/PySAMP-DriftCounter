from pysamp import register_callback
from pysamp.event import event

def register_drift_callbacks() -> None:
    register_callback("OnPlayerDriftStart", "i")
    register_callback("OnPlayerDriftUpdate", "iiiiff")
    register_callback("OnPlayerDriftEnd", "iiii")
