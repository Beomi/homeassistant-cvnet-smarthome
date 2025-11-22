from typing import Any

from homeassistant.helpers.device_registry import DeviceInfo, DeviceEntryType

from .common.cvnet_base_client import CvnetBaseClient
from ..api.visitor_api import VisitorAPI


class VisitorClient(CvnetBaseClient):
    async def _get_visitor_list(self) -> dict[str, Any]:
        return await VisitorAPI.get_visitor_list(self.session, self.config)

    async def get_visitor_image(self, file_name: str) -> bytes:
        return await VisitorAPI.get_visitor_image(self.session, self.config, file_name)

    async def get_data(self) -> dict[str, Any]:
        data = await self._request(self._get_visitor_list)

        latest_visitor = None
        if data.get("contents"):
            latest_visitor = data["contents"][0]

        return {
            "visitor_image": {
                "info": DeviceInfo(
                    identifiers={(self.config.unique_id, "visitor")},
                    entry_type=DeviceEntryType.SERVICE,
                    manufacturer="CVnet",
                    translation_key="visitor",
                ),
                "image": latest_visitor,
            }
        }
