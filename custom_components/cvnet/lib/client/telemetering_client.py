from typing import Any

from homeassistant.helpers.device_registry import DeviceInfo, DeviceEntryType

from .common.cvnet_base_client import CvnetBaseClient
from ..api.device.telemetering import TelemeteringDeviceApi
from ..model.device import TelemeteringRespond


class TelemeteringClient(CvnetBaseClient):
    async def _get_telemetering_data(self) -> TelemeteringRespond:
        return await TelemeteringDeviceApi.get_telemetering_device_detail(self.session, self.config)

    async def get_telemetering_data(self) -> TelemeteringRespond:
        return await self._request(self._get_telemetering_data)

    async def get_data(self) -> dict[str, Any]:
        data = await self.get_telemetering_data()
        return {
            "telemetering_electricity": {
                "info": DeviceInfo(
                    identifiers={(self.config.unique_id, "telemetering")},
                    entry_type=DeviceEntryType.SERVICE,
                    manufacturer="CVnet",
                    translation_key="telemetering",
                ),
                "electricity_sensor": {
                    "value": data["electricity"],
                },
            },
            "telemetering_gas": {
                "info": DeviceInfo(
                    identifiers={(self.config.unique_id, "telemetering")},
                    entry_type=DeviceEntryType.SERVICE,
                    manufacturer="CVnet",
                    translation_key="telemetering",
                ),
                "gas_sensor": {
                    "value": data["gas"],
                },
            },
            "telemetering_water": {
                "info": DeviceInfo(
                    identifiers={(self.config.unique_id, "telemetering")},
                    entry_type=DeviceEntryType.SERVICE,
                    manufacturer="CVnet",
                    translation_key="telemetering",
                ),
                "water_sensor": {
                    "value": data["water"],
                },
            },
        }
