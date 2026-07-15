import asyncio

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .device import EnabledDevicesRespond


class CvnetConfig:
    host: str
    username: str
    password: str

    unique_id: str

    def __init__(self, host: str, username: str, password: str, unique_id: str):
        self.host = host
        self.username = username
        self.password = password

        self.unique_id = unique_id


class CvnetConfigEntryRuntimeData:
    config: CvnetConfig
    enabled_devices: EnabledDevicesRespond

    def __init__(self) -> None:
        self.coordinators: list[DataUpdateCoordinator] = []
        self.listener_tasks: list[asyncio.Task] = []
