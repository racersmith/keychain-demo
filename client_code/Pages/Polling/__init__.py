from ._anvil_designer import PollingTemplate

import anvil.server

class Polling(PollingTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def timer_1_tick(self, **event_args):
        """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
        data = anvil.server.call_s('_routing_data_request', fields_requested=['server_time'])
        self.text_1.text = data
