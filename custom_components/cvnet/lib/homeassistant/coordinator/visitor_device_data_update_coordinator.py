from datetime import timedelta

from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .common.cvnet_data_update_coordinator import CvnetDataUpdateCoordinator
from ...client.visitor_client import VisitorClient
from ...model.config import CvnetConfig


class VisitorDeviceDataUpdateCoordinator(CvnetDataUpdateCoordinator):
    _client: VisitorClient

    def __init__(self, hass: HomeAssistant, config: CvnetConfig):
        super().__init__(hass, config)
        self.update_interval = timedelta(minutes=1)
        self._client = VisitorClient(async_get_clientsession(hass), config)

    @property
    def client(self) -> VisitorClient:
        return self._client
