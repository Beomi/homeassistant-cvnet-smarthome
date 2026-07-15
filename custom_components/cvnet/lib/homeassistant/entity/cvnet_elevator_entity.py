from homeassistant.components.button import ButtonEntity, ButtonEntityDescription
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo

from ...api.elevator_api import ElevatorDirection
from ...client.elevator_client import ElevatorClient
from ...model.config import CvnetConfig


class CvnetElevatorButton(ButtonEntity):
    _attr_has_entity_name = True

    def __init__(
        self,
        client: ElevatorClient,
        config: CvnetConfig,
        entity_description: ButtonEntityDescription,
        direction: ElevatorDirection,
    ) -> None:
        self.entity_description = entity_description
        self._client = client
        self._direction = direction
        self._attr_unique_id = f"{config.unique_id}_elevator_{direction}"
        self._attr_device_info = DeviceInfo(
            identifiers={(config.unique_id, "elevator")},
            entry_type=DeviceEntryType.SERVICE,
            manufacturer="CVnet",
            translation_key="elevator",
        )

    async def async_press(self) -> None:
        """Call the elevator."""
        await self._client.call(self._direction)
