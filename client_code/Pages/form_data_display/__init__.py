from ._anvil_designer import form_data_displayTemplate

import json
import time

class form_data_display(form_data_displayTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)


    def form_show(self, **event_args):
        """This method is called when the form is shown on the page"""

        fields = {
            "fields": self.route.fields,
            "local_fields": self.route.local_fields,
            "global_fields": self.route.global_fields
        }
        self.fields.content = "# Fields\n```\n" + str(json.dumps(fields, indent=2)) + "\n```"
        
        data = {
            'now': time.time(),
            'self.item': self.item,
        }
        self.data.content = "# Data\n```\n" + str(json.dumps(data, indent=2)) + "\n```"
