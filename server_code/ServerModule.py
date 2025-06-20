import anvil.server

from keychain.client import invalidate

@anvil.server.callable
def server_side_invalidate(field_or_key=None, *, path=None, auto_invalidate_paths=True):
    invalidate(field_or_key, path=path, auto_invalidate_paths=auto_invalidate_paths)
    