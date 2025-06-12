from ._anvil_designer import ProtectedTemplate
from routing import router

class Protected(ProtectedTemplate):
    def __init__(self, routing_context: router.RoutingContext, **properties):
        self.routing_context = routing_context
        properties["item"] = routing_context.data
        self.init_components(**properties)
        self.form_data_display_1.item = self.item
        self.form_data_display_1.route = routing_context.route
        self.layout.raise_event('x-refresh')

    def form_show(self, **event_args):
        """This method is called when the form is shown on the page"""
        self.layout.raise_event('x-refresh')