from ..api.elevator_api import ElevatorApi, ElevatorDirection
from .common.cvnet_base_client import CvnetBaseClient


class ElevatorClient(CvnetBaseClient):
    async def call(self, direction: ElevatorDirection) -> None:
        """Call the elevator after refreshing an expired CVnet session if needed."""

        async def _call() -> None:
            await ElevatorApi.call(self.session, self.config, direction)

        await self._request(_call)
