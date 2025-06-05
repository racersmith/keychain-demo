from ._anvil_designer import cache_displayTemplate

from routing.router import _cached
from keychain.client.cache import _DATA, _FIELDS, _GROUPS

import json


class cache_display(cache_displayTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.refresh()

    def refresh(self, *args, **kwargs):
        lines = list()

        lines.append("# Keychain")
        lines.append("## Global Fields")
        for field in _FIELDS:
            lines.append(f"* {field}")

        lines.append("\n## Cache")
        cache_str = "```\n" + json.dumps(_DATA, indent=2) + "\n```"
        lines.append(cache_str)

        lines.append("\n## Groups")
        # lines.append(json.dumps(_GROUPS, indent=4))
        group_data = {group: list(keys) for group, keys in _GROUPS.items()}
        group_data_str = "```\n" + json.dumps(group_data, indent=2) + "\n```"
        lines.append(group_data_str)
        
        lines.append("# Routing")
        lines.append("## Cached Form Data")
        form_data = {key: value.data for key, value in _cached.CACHED_DATA.items()}
        form_data_str = "```\n" + json.dumps(form_data, indent=2) + "\n```"
        lines.append(form_data_str)
        
        self.text.content = "\n".join(lines)

        
