from setuptools import setup, find_packages

setup(
    name="marketpulse",
    version="0.1.0",
    packages=find_packages(include=["api", "api.*", "scheduler", "scheduler.*", "delivery", "delivery.*", "pipeline", "pipeline.*"]),
    package_dir={
        "marketpulse.api": "api",
        "marketpulse.scheduler": "scheduler",
        "marketpulse.delivery": "delivery",
        "marketpulse.pipeline": "pipeline"
        # Add any other root folders (e.g., "marketpulse.persistence": "persistence") if you have them
    },
)
