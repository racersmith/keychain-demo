import anvil.server
from keychain.server import register_data_request, Flatten

import time


def admin_check():
    print(anvil.server.session)
    locked = anvil.server.session.get('admin', False)
    print(f"Admin Check: {locked}")
    return locked


@anvil.server.callable
def set_lock_state(admin: bool):
    anvil.server.session['admin'] = bool(admin)
    print(anvil.server.session)


@register_data_request(field="the answer to life the universe and everything")
def get_the_answer(*args, **loader_args):
    print("get_the_answer", loader_args["params"])
    return 42


@register_data_request(
    field="what is the question", permission=admin_check, quiet=False
)
def get_the_question(*args, **loader_args):
    print("get_the_question", loader_args["params"])
    # raise LookupError("The question remains unknown.")
    return "Starting Deep Thought...Result expected in 7.5 Million Years."


@register_data_request(field=["account", "name", "email", "phone"])
def get_account_data(*args, **loader_args):
    """Allow multiple fields to resolve to the same function for use cases like this.
    Here I'm using the Flatten marker that will then be flattened in the data reponse.
    This might be a complication that without much benefit.
    This could be interesting if we namespaced keys...
    ie.
        'account' -> {'name': name, 'email': email, 'phone': phone}
        'account.email' -> email
    """
    print("get_account_data", loader_args.get("params", None))
    return Flatten(name="Arther", email="arther@galaxyguides.com", phone="987-654-3210")


@register_data_request(field=["first_load", "server_time"])
def get_time(*args, **loader_args):
    print("get_time", loader_args.get("params", None))
    return time.time()


@register_data_request(field="something_private", permission=admin_check, quiet=True)
def get_private_data(*args, **loader_args):
    print("get_private_data", loader_args["params"])
    return "Private Data from server"


@register_data_request(field="private_{private_id}")
def get_private_value(*args, **loader_args):
    print("get_private_value", loader_args["params"])
    return f"P{3 * str(loader_args['params'].get('private_id'))}V"
