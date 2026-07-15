import json
from typing import Literal

import aiohttp

from ..model.config import CvnetConfig
from ..model.exception import UnauthorizedException, UnknownException

type ElevatorDirection = Literal["up", "down"]


class ElevatorApi:
    @staticmethod
    async def call(
        websession: aiohttp.ClientSession,
        config: CvnetConfig,
        direction: ElevatorDirection,
    ) -> None:
        """Call the elevator in the requested direction."""
        async with websession.post(
            f"https://{config.host}/cvnet/mobile/elevator_call.do",
            data={"control": direction},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        ) as response:
            if response.status != 200:
                raise UnknownException(f"Elevator call returned HTTP {response.status}")

            try:
                data = json.loads(await response.text())
            except json.JSONDecodeError as err:
                # CVnet commonly returns the login page after a session expires.
                raise UnauthorizedException("Elevator call session expired") from err

        if data.get("result") in (None, False, 0, "0"):
            raise UnauthorizedException("Elevator call was not authenticated")

        if str(data.get("status")) != "1":
            raise UnknownException(data.get("message", "Elevator call failed"))
