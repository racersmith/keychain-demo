from routing.router import Route, Redirect
from keychain.client import AutoLoad


ADMIN = False


class RootRoute(Route):
    path = "/"

    def before_load(self, **loader_args):
        raise Redirect(path="/home")


class HomeRoute(AutoLoad):
    path = "/home"
    form = "Pages.Home"
    fields = [
        "first_load",
        "the answer to life the universe and everything",
        "field_without_fn",
    ]
    strict = False


class AccountRoute(AutoLoad):
    path = "/account"
    form = "Pages.Account"
    strict = False
    fields = [
        "first_load",
        "the answer to life the universe and everything",
        "name",
        "email",
    ]


class PrivateIdRoute(AutoLoad):
    path = "/private/:private_id"
    form = "Pages.Private"
    cache_data = False

    global_fields = ["private_{private_id}"]
    remap_fields = {
        "private_{private_id}": "private",
    }


class PrivateRoute(AutoLoad):
    path = "/private"
    form = "Pages.Private"
    strict = False
    cache_data = False
    fields = ["name", "something_private", "field_without_fn"]


class StrictRoute(AutoLoad):
    path = "/strict"
    form = "Pages.Strict"
    strict = True
    fields = ["field_without_fn"]  # This will raise a LookupError


class PollingRoute(Route):
    path = "/polling"
    form = "Pages.Polling"


class ProtectedRoute(AutoLoad):
    path = "/protected"
    form = "Pages.Protected"
    global_fields = ["what is the question"]
    permission_error_path = "/home"
    cache_data = False


class OptionsRoute(AutoLoad):
    path = "/option"
    form = "Pages.PageOptions.Option1"
    fields = ["name", "first_load"]
    cache_data = False
    cache_form = False

    def before_load(self, *args, **loader_args):
        """Change form and data required at time of navigation"""
        if ADMIN:
            self.form = "Pages.PageOptions.Option1"
            self.fields = ["name"]
        else:
            self.form = "Pages.PageOptions.Option2"
            self.fields = ["first_load"]
