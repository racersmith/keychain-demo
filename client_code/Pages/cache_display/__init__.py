from ._anvil_designer import cache_displayTemplate

from routing.router import _cached
from keychain.data_finder.cache import _DATA, _FIELDS, _GROUPS

import json


class cache_display(cache_displayTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.refresh()

    def refresh(self, *args, **kwargs):
        lines = ["==Router Cached Form Data=="]
        for key, value in _cached.CACHED_DATA.items():
            lines.append(f"{key}:\n{json.dumps(value.data, indent=4)}\n")

        lines.append("==Global Keys==")
        lines.append("\n".join(_FIELDS))

        lines.append("\n==Global Cache==")
        lines.append(json.dumps(_DATA, indent=4))
        self.text_1.text = "\n".join(lines)
