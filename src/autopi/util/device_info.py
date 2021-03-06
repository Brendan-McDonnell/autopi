"""Utilities to retrieve device information."""

import subprocess
from hashlib import sha256

from util.config import Config


def get_dev_id() -> str:
    """Get device ID from boot drive.

    Returns:
        id (str): unique device id

    Raises:
        OSError: file in boot drive could not be read
    """
    with open(Config.DEV_ID_FILE) as f:
        lines = f.readlines()
    return "".join(lines).strip()


def get_hw_info() -> list:
    """Return 4 lines of cpu serial and hardware data."""
    with open(Config.HW_ID_SOURCE_FILE) as f:
        lines = f.readlines()
    return lines[Config.HW_ID_START_LINE : Config.HW_ID_STOP_LINE]


def get_hw_id() -> str:
    """Return standard hardware ID hashed from the last 4 lines of /proc/cpuinfo."""
    info_lines = get_hw_info()
    raw = "".join(info_lines).encode("utf-8")
    return sha256(raw).hexdigest()


def is_service_up(service: str) -> bool:
    """Return bool representing whether service is up.

    Obtains status from 'service SERVICE_STR status' return code. The return codes are different per-service, but 0 should always imply UP. 0 => UP, not 0 => DOWN.

    Args:
        service (str): service name as in linux command 'service SERVICE_STR status'

    Returns:
        bool: service is up
    """
    result = subprocess.run(["service", service, "status"], capture_output=True, check=False)
    return result.returncode == 0
