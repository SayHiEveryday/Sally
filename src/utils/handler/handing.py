import nextcord
from utils.core.log import get_logger
import typing as t

log = get_logger(__name__)

async def safe_dm(coro: t.Coroutine) -> None:
    try:
        await coro
    except nextcord.HTTPException as discord_exc:
        log.trace(f"DM dispatch failed on status {discord_exc.status} with code: {discord_exc.code}")
        if discord_exc.code != 50_007:  # If any reason other than disabled DMs
            raise