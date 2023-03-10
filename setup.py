from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hybrow_demo/__init__.py
from hybrow_demo import __version__ as version

setup(
	name="hybrow_demo",
	version=version,
	description="testing",
	author="vikas moin",
	author_email="vikas.moin@hybrowlabs.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
