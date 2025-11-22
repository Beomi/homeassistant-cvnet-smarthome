import base64
import json
from typing import Any

from aiohttp import ClientSession

from ..model.config import CvnetConfig


class VisitorAPI:
    @staticmethod
    async def get_visitor_list(
        session: ClientSession, config: CvnetConfig
    ) -> dict[str, Any]:
        """Get visitor list."""
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        # The API expects form data for pagination
        data = {"pageNo": "1", "rows": "30"}

        async with session.post(
            f"https://{config.host}/cvnet/mobile/visitor_list.do",
            headers=headers,
            data=data,
        ) as response:
            text = await response.text()
            return json.loads(text)

    @staticmethod
    async def get_visitor_image(
        session: ClientSession, config: CvnetConfig, file_name: str
    ) -> bytes:
        """Get visitor image."""
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        data = {"file_name": file_name}

        async with session.post(
            f"https://{config.host}/cvnet/mobile/visitor_content.do",
            headers=headers,
            data=data,
        ) as response:
            text = await response.text()
            json_data = json.loads(text)
            # The image is returned as a base64 encoded string in the "image" field
            if "image" in json_data:
                return base64.b64decode(json_data["image"])
            return b""
