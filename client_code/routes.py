from routing.router import Route, Redirect
from routing_data.data_finder import AutoLoad, find_global_fields


class RootRoute(Route):
    path = "/"

    def before_load(self, **loader_args):
        raise Redirect(path="/home")


class HomeRoute(AutoLoad):
    path = "/home"
    form = "Pages.Home"
    fields = ["first_load", "the answer to everything"]


class AccountRoute(AutoLoad):
    path = "/account"
    form = "Pages.Account"
    strict = False
    fields = ["first_load", "the answer to life", "name"]


class PrivateIdRoute(AutoLoad):
    path = "/private/:private_id"
    form = "Pages.Private"
    strict = False
    cache_data = False  # just for demo purposes
    
    global_fields = ["private_{private_id}"]
    remap_fields = {"private_{private_id}": "private"}


class PrivateRoute(AutoLoad):
    path = "/private"
    form = "Pages.Private"
    strict = False    
    fields = ["name", "something_private"]


class ProtectedRoute(AutoLoad):
    path = "/protected"
    form = "Pages.Protected"
    fields = ["what is the question"]


# This could be more tightly integrated so this is not needed here...
find_global_fields()
