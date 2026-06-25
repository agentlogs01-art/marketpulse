import os
import sys

# Force the /app root into the Python search space inside Gunicorn's core process
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Standard production binding configurations
bind = "0.0.0.0:" + os.getenv("PORT", "8080")
workers = 2
