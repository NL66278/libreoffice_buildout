from setuptools import setup

setup(
    name = "mkdir_recipe",
    entry_points = {'zc.buildout': ['mkdir = mkdir:Mkdir']},
    )
