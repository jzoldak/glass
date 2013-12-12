"""Setup for glass XBlock."""

import os
from setuptools import setup


def package_data(pkg, root):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for dirname, _, files in os.walk(os.path.join(pkg, root)):
        for fname in files:
            data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='glass-xblock',
    version='0.1',
    description='glass XBlock',   # TODO: write a better description.
    packages=[
        'glass',
    ],
    install_requires=[
        'XBlock',
        'requests',
    ],
    entry_points={
        'xblock.v1': [
            'glass = glass:GlassXBlock',
        ]
    },
    package_data=package_data("glass", "static"),
)
