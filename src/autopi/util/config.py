"""Temporary module for reading a dummy configuration."""

import os


# TODO REPLACE ME
def get_api_url() -> str:
    """Return api url as string.

    This is a temporary placeholder.

    Defult API_URL is 'http://localhost:8000/. If 'API_URL' is available in os.environ, then that setting is used. Otherwise, if /autopi.config exists, it will check for a 'API_URL=...' line.

    Returns:
        str: the api url.
    """
    api_url = "http://localhost:8000/"
    if "API_URL" in os.environ:
        api_url = os.environ["API_URL"]
    else:
        try:
            with open("/autopi.config") as f:
                lines = f.readlines()
        except OSError:
            # TODO determine + implement appropriate behavior; if it isn't scrapped outright
            pass
        else:
            for line in lines:
                ln = line.strip()
                if ln.startswith("API_URL="):
                    api_url = ln[8:].strip()  # TODO re-write this glorious code
    return api_url