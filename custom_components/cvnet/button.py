from homeassistant.components.button import ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .lib.api.elevator_api import ElevatorDirection
from .lib.client.elevator_client import ElevatorClient
from .lib.homeassistant.entity.cvnet_elevator_entity import CvnetElevatorButton
from .lib.model.config import CvnetConfigEntryRuntimeData

DESCRIPTIONS: tuple[tuple[ButtonEntityDescription, ElevatorDirection], ...] = (
    (
        ButtonEntityDescription(
            key="elevator_up",
            translation_key="elevator_up",
        ),
        "up",
    ),
    (
        ButtonEntityDescription(
            key="elevator_down",
            translation_key="elevator_down",
        ),
        "down",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry[CvnetConfigEntryRuntimeData],
    async_add_entities: AddEntitiesCallback,
) -> None:
    runtime_data = entry.runtime_data
    if not runtime_data.enabled_devices.get("isElevator", False):
        return

    client = ElevatorClient(async_get_clientsession(hass), runtime_data.config)
    async_add_entities(
        [
            CvnetElevatorButton(client, runtime_data.config, description, direction)
            for description, direction in DESCRIPTIONS
        ]
    )
