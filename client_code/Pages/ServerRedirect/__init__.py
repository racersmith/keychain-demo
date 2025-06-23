from ._anvil_designer import ServerRedirectTemplate
class ServerRedirect(ServerRedirectTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
