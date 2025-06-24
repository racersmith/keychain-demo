from routing.router import launch
from .import routes
from keychain.client import initialize_cache

if __name__ == "__main__":
    launch()
    
    # This initializes
    initialize_cache()
