from datetime import datetime
from typing import Any

from homeassistant.components.image import ImageEntity, ImageEntityDescription

from homeassistant.util import dt as dt_util

from ..coordinator.visitor_device_data_update_coordinator import (
    VisitorDeviceDataUpdateCoordinator,
)
from .cvnet_entity import CvnetEntity


class CvnetVisitorImage(CvnetEntity, ImageEntity):
    coordinator: VisitorDeviceDataUpdateCoordinator

    def __init__(
        self,
        coordinator: VisitorDeviceDataUpdateCoordinator,
        entity_description: ImageEntityDescription,
        coordinator_data_key: str,
    ) -> None:
        super().__init__(coordinator, entity_description, coordinator_data_key)
        ImageEntity.__init__(self, coordinator.hass)
        self._attr_name = None
        self._attr_content_type = "image/jpeg"
        self._cached_image: bytes | None = None
        self._cached_file_name: str | None = None

    @property
    def _image_data(self) -> dict[str, Any] | None:
        return self._data.get("image")

    @property
    def image_last_updated(self) -> datetime | None:
        """The time when the image was last updated."""
        data = self._image_data
        if not data:
            return None

        date_time_str = data.get("date_time")
        if not date_time_str:
            return None

        try:
            # Format: "2025-11-20 10:50"
            dt = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M")
            # Assume local time, convert to aware datetime
            return dt_util.as_local(dt)
        except ValueError:
            return None

    async def async_image(self) -> bytes | None:
        data = self._image_data
        if not data:
            return None

        file_name = data.get("file_name")
        if not file_name:
            return None

        if self._cached_file_name == file_name and self._cached_image:
            return self._cached_image

        image = await self.coordinator.client.get_visitor_image(file_name)
        if image:
            self._cached_image = image
            self._cached_file_name = file_name

        return image
