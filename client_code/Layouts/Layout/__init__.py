import anvil.server

from keychain.client import invalidate
from ... import routes
from ._anvil_designer import LayoutTemplate

class Layout(LayoutTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.add_event_handler('x-refresh', self.cache_display.refresh)
        self.lock_switch.selected = routes.ADMIN

    def lock_switch_change(self, **event_args):
        """This method is called when the state of the component is changed."""
        routes.ADMIN = self.lock_switch.selected
        anvil.server.call_s('set_lock_state', routes.ADMIN)
        invalidate("what is the question")

