import os
import sys

# Get the absolute root path (/app)
root_dir = os.path.dirname(os.path.abspath(__file__))

# If the virtual wrapper isn't in sys.modules, map it to root
if "marketpulse" not in sys.modules:
    import types
    # Create a dynamic module container named 'marketpulse'
    mp_module = types.ModuleType("marketpulse")
    mp_module.__path__ = [root_dir]
    sys.modules["marketpulse"] = mp_module
