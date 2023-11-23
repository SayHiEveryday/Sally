import nextcord
from utils.core.log import get_logger
import typing as t

log = get_logger(__name__)

async def safe_dm(coro: t.Coroutine) -> None:
    """
    Execute `coro` ignoring disabled DM warnings.

    The 50_0007 error code indicates that the target user does not accept DMs.
    As it turns out, this error code can appear on both 400 and 403 statuses,
    we therefore catch any Discord exception.

    If the request fails on any other error code, the exception propagates,
    and must be handled by the caller.
    """
    try:
        await coro
    except nextcord.HTTPException as discord_exc:
        log.trace(f"DM dispatch failed on status {discord_exc.status} with code: {discord_exc.code}")
        if discord_exc.code != 50_007:  # If any reason other than disabled DMs
            raise