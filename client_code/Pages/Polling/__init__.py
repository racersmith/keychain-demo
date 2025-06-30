from ._anvil_designer import PollingTemplate

from keychain.client import fetch


class Polling(PollingTemplate):
    def __init__(self, **properties):
        self.forced = False
        self.init_components(**properties)
        

    def timer_1_tick(self, **event_args):
        """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
        data = fetch(["first_load"], force_update=self.forced)
        self.text_1.text = data
        self.heartbeat_icon.selected = ~self.heartbeat_icon.selected
