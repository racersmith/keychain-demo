from ._anvil_designer import form_data_displayTemplate

import json
import time

class form_data_display(form_data_displayTemplate):
    def __init__(self, **properties):
        self.route = None
        self.init_components(**properties)


    def form_show(self, **event_args):
        """This method is called when the form is shown on the page"""

        keys = ["fields", "local_fields", "global_fields", "remap_fields"]
        
        fields = dict()
        for key in keys:
            fields[key] = getattr(self.route, key)
            
        self.fields.content = "# Fields\n```\n" + str(json.dumps(fields, indent=2)) + "\n```"
        
        data = {
            'now': time.time(),
            'self.item': self.item,
        }
        self.data.content = "# Data\n```\n" + str(json.dumps(data, indent=2)) + "\n```"
