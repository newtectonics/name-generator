from setuptools import setup

setup(
    name="namegen",
    version="0.1.0",
    description="Generate random human names",
    packages=["namegen"],
    entry_points={
        "console_scripts": [
            "namegen = namegen.generator:generate_name"
        ]
    },
)