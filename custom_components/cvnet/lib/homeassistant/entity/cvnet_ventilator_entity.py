from typing import Any, Coroutine, Callable

from homeassistant.components.climate import FAN_LOW, FAN_MEDIUM, FAN_HIGH
from homeassistant.components.fan import FanEntity, FanEntityFeature, FanEntityDescription
from homeassistant.core import callback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.util.percentage import ordered_list_item_to_percentage, percentage_to_ordered_list_item

from .cvnet_entity import CvnetEntity

_FAN_TYPES = [FAN_LOW, FAN_MEDIUM, FAN_HIGH]

class CvnetVentilatorEntity(CvnetEntity, FanEntity):
    _wind_level = {
        FAN_LOW: 1,
        FAN_MEDIUM: 2,
        FAN_HIGH: 3,
    }

    _set_state_function: Callable[[bool, int], Coroutine]
    _attr_custom_speed: str | None = None

    def __init__(self, coordinator: DataUpdateCoordinator[dict[str, Any]], entity_description: FanEntityDescription,
                 coordinator_data_key: str):
        super().__init__(coordinator, entity_description, coordinator_data_key)

        self._attr_name = None

        data = coordinator.data[coordinator_data_key]
        self._set_state_function = data[entity_description.key]["set_state_function"]

        self._attr_supported_features = FanEntityFeature.SET_SPEED | FanEntityFeature.TURN_ON | FanEntityFeature.TURN_OFF
        self._attr_custom_speed = data[entity_description.key]["state"]

        self._attr_is_on = data[entity_description.key]["is_on"]

    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None:
        self._attr_is_on = True
        self._attr_custom_speed = percentage_to_ordered_list_item(_FAN_TYPES, percentage) if percentage != 0 and percentage is not None else FAN_LOW
        self.async_write_ha_state()

        await self._set_state_function(self._attr_is_on, self._wind_level[self._attr_custom_speed])

    async def async_turn_off(self, percentage: int | None = None, preset_mode: str | None = None,
                             **kwargs: Any) -> None:
        self._attr_is_on = False
        self._attr_custom_speed = None
        self.async_write_ha_state()

        await self._set_state_function(self._attr_is_on, 0)

    async def async_set_percentage(self, percentage: int) -> None:
        if percentage > 0:
            wind_level = percentage_to_ordered_list_item(_FAN_TYPES, percentage)
            self._attr_custom_speed = wind_level
            self._attr_is_on = True
        else:
            wind_level = None
            self._attr_custom_speed = None
            self._attr_is_on = False
        self.async_write_ha_state()

        await self._set_state_function(self._attr_is_on, self._wind_level.get(wind_level, 0))

    @property
    def percentage(self) -> int | None:
        if self._attr_custom_speed is None:
            return None
        return ordered_list_item_to_percentage(_FAN_TYPES, self._attr_custom_speed)

    @property
    def speed_count(self) -> int:
        return len(_FAN_TYPES)

    @callback
    def _handle_coordinator_update(self):
        """Handle updated data from the coordinator."""
        data = self._data

        self._attr_custom_speed = data[self.entity_description.key]["state"]
        self._attr_is_on = data[self.entity_description.key]["is_on"]

        super()._handle_coordinator_update()
