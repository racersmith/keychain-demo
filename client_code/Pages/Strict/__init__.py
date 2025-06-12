from ._anvil_designer import StrictTemplate

class Strict(StrictTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
