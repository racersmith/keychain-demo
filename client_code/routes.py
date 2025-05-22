from routing.router import Route, Redirect
from routing_data.data_finder import AutoLoad, find_global_fields

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
    strict = False
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


class ProtectedRoute(AutoLoad):
    path = "/protected"
    form = "Pages.Protected"
    fields = ["what is the question"]


# class Option1Route(AutoLoad):
#     path = "/option_1"
#     form = "Pages.PageOptions.Option1"
#     fields = ["first_load"]

# class Option2Route(AutoLoad):
#     path = "/option_2"
#     form = "Pages.PageOptions.Option2"
#     fields = ["name"]


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

    # def load_form(self, _, routing_context):
    #     navigate("/option_2", replace=True, form_properties=routing_context.form_properties)


# This could be more tightly integrated so this is not needed here...
find_global_fields()
