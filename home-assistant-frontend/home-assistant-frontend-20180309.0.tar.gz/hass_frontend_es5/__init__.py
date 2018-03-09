"""Frontend for Home Assistant."""
import os
from user_agents import parse

FAMILY_MIN_VERSION = {
    'Chrome': 54,          # Object.values
    'Chrome Mobile': 54,
    'Firefox': 47,         # Object.values
    'Firefox Mobile': 47,
    'Opera': 41,           # Object.values
    'Edge': 14,            # Array.prototype.includes added in 14
    'Safari': 10,          # Many features not supported by 9
}


def where():
    """Return path to the frontend."""
    return os.path.dirname(__file__)


def version(useragent):
    """Get the version for given user agent."""
    useragent = parse(useragent)

    # on iOS every browser is a Safari which we support from version 11.
    if useragent.os.family == 'iOS':
        # Was >= 10, temp setting it to 12 to work around issue #11387
        return useragent.os.version[0] >= 12

    version = FAMILY_MIN_VERSION.get(useragent.browser.family)
    return version and useragent.browser.version[0] >= version
VERSION = 'd93a0f7a5de3682500b1a714ece69a916a663939'
CREATED_AT = 1520555930
FINGERPRINTS = {
    "config": "c77a7be32715f8e5a4357554f781b081",
    "dev-event": "33c97e02377b68161b0df3420369a649",
    "dev-info": "cd740e514f472a2f6ce57f077eb2df98",
    "dev-mqtt": "9363c534af8f7a21919c5f646ffc9b71",
    "dev-service": "bda9a01286fe0eddd1250067c62e117b",
    "dev-state": "60b799a561c3e2230617b62e794969a8",
    "dev-template": "1aba8db0b3d638a09919567232e615d7",
    "hassio": "2a967492d78538a12ff6738879e68e62",
    "history": "da35b904ceac75993ca852431b3d26f8",
    "iframe": "185480826c02fec59d9ad045abee15f4",
    "kiosk": "4d15ef5a5be516d512bb8a5ba879c3b0",
    "logbook": "579cbedb83e7146c19195f002f6acdf8",
    "mailbox": "ceadcf082f949a3e409b4db5aca5579e",
    "map": "1f526fe98780ac172895321656aaf773",
    "shopping-list": "a5a7dc931be6beb757bf18e4d66c5446"
}
