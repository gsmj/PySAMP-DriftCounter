from pysamp import call_native_function


def drift_set_update_delay(delay: int) -> None:
    return call_native_function("DriftSet_UpdateDelay", delay)

def drift_get_update_delay() -> int:
    return call_native_function("DriftGet_UpdateDelay")

def drift_set_minimal_speed(speed: float, player_id: int = -1) -> None:
    return call_native_function("DriftSet_MinimalSpeed", speed, player_id)

def drift_set_minimal_angle(angle: float, player_id: int = -1) -> None:
    return call_native_function("DriftSet_MinimalAngle", angle, player_id)

def drift_set_maximal_speed(speed: float, player_id: int = -1) -> None:
    return call_native_function("DriftSet_MaximalSpeed", speed, player_id)

def drift_set_maximal_angle(angle: float, player_id: int = -1) -> None:
    return call_native_function("DriftSet_MaximalAngle", angle, player_id)

def drift_set_start_end_delay(delay: int, player_id: int = -1) -> None:
    return call_native_function("DriftSet_StartEndDelay", delay, player_id)

def drift_get_start_end_delay(player_id: int = -1) -> int:
    return call_native_function("DriftGet_StartEndDelay", player_id)

def drift_set_divider(divider: int, player_id: int = -1) -> None:
    return call_native_function("DriftSet_Divider", divider, player_id)

def drift_set_ged_divider(player_id: int = -1) -> int:
    return call_native_function("DriftGet_Divider", player_id)

def drift_set_damage_check(enable: bool = True, player_id: int = -1, max_healt_loose: float = 0.0) -> None:
    return call_native_function("DriftSet_DamageCheck", enable, player_id, max_healt_loose)

def is_player_drifting(player_id: int) -> bool:
    return call_native_function("IsPlayerDrifting", player_id)

def is_player_drifting_precise(player_id: int) -> bool:
    """
    This function is more accurate than `is_player_drifting()`.
    The function actually tells you that the car is actually drifting, not the player.
    """
    return call_native_function("IsPlayerDrifting_precise", player_id)

def drift_add_flag(x: float, y: float, z: float) -> int:
    return call_native_function("Drift_AddFLAG", x, y, z)

def drift_disable_flag(flag_id: int) -> None:
    return call_native_function("Drift_DisableFLAG", flag_id)

def drift_delete_flag(flag_id: int) -> None:
    return call_native_function("Drift_DeleteFLAG", flag_id)

def drift_enable_flag(flag_id: int) -> None:
    return call_native_function("Drift_EnableFLAG", flag_id)

def drift_move_flag(flag_id: int, x: float, y: float, z: float) -> None:
    return call_native_function("Drift_MoveFLAG", flag_id, x, y, z)

def drift_set_check_for_flag(enabled: bool = True, player_id: int = -1) -> None:
    return call_native_function("Drift_SetCheckForFlags", enabled, player_id)

def drift_get_check_for_flags(player_id: int = -1):
    return call_native_function("Drift_GetCheckForFlags", player_id)

def drift_set_global_check(enable: bool = True) -> None:
    return call_native_function("Drift_SetGlobalCheck", enable)

def drift_get_global_check() -> bool:
    return call_native_function("Drift_GetGlobalCheck")

def drift_set_player_check(player_id: int = -1, enable: bool = True) -> None:
    return call_native_function("Drift_SetPlayerCheck", player_id, enable)

def drift_get_player_check(player_id: int = -1):
    return call_native_function("Drift_GetPlayerCheck", player_id)

def drift_set_backwards_check(enabled: bool = True, player_id: int = -1) -> None:
    return call_native_function("Drift_SetBackwardsCheck", enabled, player_id)

def drift_get_backwards_check(playerid: int = -1):
    return call_native_function("Drift_GetBackwardsCheck", playerid)

def drift_set_max_health_loose(max_loose: float = 0.0, player_id: int = -1) -> None:
    return call_native_function("Drift_SetDriftMaxHealthLoose", max_loose, player_id)

def drift_get_version() -> str:
    return call_native_function("Private_DriftGetVersion")

def drift_allow_model(model_id: int) -> None:
    return call_native_function("Drift_AllowModel", model_id)

def drift_disallow_model(model_id: int) -> None:
    return call_native_function("Drift_DisallowModel", model_id)

def dirft_clear_model_list() -> None:
    return call_native_function("Drift_ClearModelList")

def drift_restore_model_list() -> None:
    return call_native_function("Drift_ResetDefaultModelList")
