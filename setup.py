
from setuptools import setup, find_packages
from krmd.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='krmd',
    version=VERSION,
    description='Simple command reminder application',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Kerem Demirturk',
    author_email='keremdemirtrk@gmail.com',
    url='https://github.com/keremdemirtrk/krmd',
    license='GNU General Public License version 3',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'krmd': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        krmd = krmd.main:main
    """,
)
