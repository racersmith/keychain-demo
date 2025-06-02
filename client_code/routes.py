from routing.router import Route, Redirect
from routing_data.data_finder import AutoLoad, initialize_cache

import time


class RootRoute(Route):
    path = "/"

    def before_load(self, **loader_args):
        raise Redirect(path="/home")


class HomeRoute(AutoLoad):
    path = "/home"
    form = "Pages.Home"
    fields = ["first_load", "the answer to everything", "field without fn"]
    strict = False


class AccountRoute(AutoLoad):
    path = "/account"
    form = "Pages.Account"
    strict = False
    fields = ["first_load", "the answer to life", "name", "email"]


class PrivateIdRoute(AutoLoad):
    path = "/private/:private_id"
    form = "Pages.Private"
    cache_data = False  # just for demo purposes

    global_fields = ["private_{private_id}"]
    remap_fields = {
        "private_{private_id}": "private",
    }


class PrivateRoute(AutoLoad):
    path = "/private"
    form = "Pages.Private"
    strict = False
    fields = ["name", "something_private"]


class StrictRoute(AutoLoad):
    path = "/strict"
    form = "Pages.Strict"
    strict = True
    fields = ["field without fn"]  # This will raise a LookupError


class PollingRoute(Route):
    path = "/polling"
    form = "Pages.Polling"


class ProtectedRoute(AutoLoad):
    path = "/protected"
    form = "Pages.Protected"
    fields = ["what is the question"]
    permission_error_path = "/home"


class OptionsRoute(AutoLoad):
    path = "/option"
    form = "Pages.PageOptions.Option1"
    fields = ["name", "first_load"]
    cache_data = False

    def before_load(self, *args, **loader_args):
        """Change form and data required at time of navigation"""
        if time.time() % 10 < 5:
            self.form = "Pages.PageOptions.Option1"
            self.fields = ["name"]
        else:
            self.form = "Pages.PageOptions.Option2"
            self.fields = ["first_load"]


# This initializes
initialize_cache()
