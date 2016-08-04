import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="django-cegf-widgets",
    version="0.0.1",
    author="Cesar Gonzalez Fernandez",
    author_email="cesar.gon.fer@gmail.com",
    description="A minimal set of widgets that i need in some moments.",
    keywords="django widget",
    packages=['cegfforms', 'tests'],
    long_description="A minimal set of widgets that i need in some moments.",
    include_package_data=True,
)