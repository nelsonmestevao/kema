import setuptools
from kema import VERSION

setuptools.setup(
    name="kema",
    version=VERSION,
    author="Nelson Estevão",
    author_email="hello@estevao.xyz",
    description="A small package to help setting up projects",
    url="https://github.com/nelsonmestevao/kema",
    packages=setuptools.find_packages(),
    data_files=[
        ("config", ["kema/kema.ini"]),
        ("templates",
         ["kema/templates/header.tmpl.h", "kema/templates/source.tmpl.c"]),
    ],
    install_requires=["docopt==0.6.2"],
    entry_points={"console_scripts": ["kema = kema.app:main"]},
)
