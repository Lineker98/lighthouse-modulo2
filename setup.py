from setuptools import setup

setup(
    name="site checker",
    version="1.0.0",
    install_requires=["Click"],
    entry_points={"console_scripts": ["sitechecker = sitechecker.__main__:main"]},
)
