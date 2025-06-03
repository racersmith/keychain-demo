from ._anvil_designer import PollingTemplate

from routing_data.data_finder import fetch_from_server


class Polling(PollingTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def timer_1_tick(self, **event_args):
        """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
        data = fetch_from_server("server_time")
        self.text_1.text = data
