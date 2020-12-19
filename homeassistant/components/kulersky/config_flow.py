"""Config flow for Kuler Sky."""
import logging

import pykulersky

from homeassistant import config_entries
from homeassistant.helpers import config_entry_flow

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def _async_has_devices(hass) -> bool:
    """Return if there are devices that can be discovered."""
    try:
        devices = await pykulersky.discover()
    except pykulersky.PykulerskyException as exc:
        _LOGGER.error("Unable to discover nearby Kuler Sky devices: %s", exc)
        return False
    return len(devices) > 0


config_entry_flow.register_discovery_flow(
    DOMAIN, "Kuler Sky", _async_has_devices, config_entries.CONN_CLASS_LOCAL_POLL
)
