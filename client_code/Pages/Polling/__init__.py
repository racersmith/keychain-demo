from ._anvil_designer import PollingTemplate

from keychain.client import fetch

import json


class Polling(PollingTemplate):
    def __init__(self, **properties):
        self.forced = False
        self.init_components(**properties)
        

    def timer_1_tick(self, **event_args):
        """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
        # first_load is part of global cache and will only be updated if forced.
        # server_time is not part of global cache so it will always be requested from the server
        data = fetch(["first_load", "server_time"], force_update=self.forced)
        self.text_1.text = json.dumps(data, indent=2)
        self.heartbeat_icon.selected = ~self.heartbeat_icon.selected
