import logging

from homeassistant.components.image import ImageEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import CvnetConfigEntryRuntimeData
from .lib.homeassistant.coordinator.visitor_device_data_update_coordinator import (
    VisitorDeviceDataUpdateCoordinator,
)
from .lib.homeassistant.entity.cvnet_visitor_entity import CvnetVisitorImage

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    runtime_data: CvnetConfigEntryRuntimeData = entry.runtime_data

    # Find the visitor coordinator from runtime_data
    coordinator = None
    for c in runtime_data.coordinators:
        if isinstance(c, VisitorDeviceDataUpdateCoordinator):
            coordinator = c
            break

    if not coordinator:
        _LOGGER.warning("Visitor coordinator not found")
        return

    async_add_entities(
        [
            CvnetVisitorImage(
                coordinator,
                ImageEntityDescription(
                    key="visitor_image",
                    translation_key="visitor",
                    has_entity_name=True,
                    name=None,
                ),
                "visitor_image",
            )
        ]
    )
