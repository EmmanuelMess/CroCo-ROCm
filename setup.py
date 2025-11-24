from pathlib import Path
from setuptools import setup

curope = Path(__file__).parent / "models" / "curope"

setup(
    install_requires=[
        "torch",
        "torchvision",
        f"curope @ {curope.as_uri()}",
    ],
)
