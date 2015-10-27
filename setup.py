import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

__author__ = 'eamonnmaguire'

test_requirements = [
    'pytest>=2.7.0',
    "pytest-cache>=1.0",
    'pytest-cov>=1.8.0',
    'pytest-pep8>=1.0.6',
    'coverage>=3.7.1',
]


class PyTest(TestCommand):
    """PyTest Test."""

    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        """Init pytest."""
        TestCommand.initialize_options(self)
        self.pytest_args = []

        from ConfigParser import ConfigParser

        config = ConfigParser()
        config.read('pytest.ini')
        self.pytest_args = config.get('pytest', 'addopts').split(' ')

    def finalize_options(self):
        """Finalize pytest."""
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """Run tests."""
        # import here, cause outside the eggs aren't loaded
        import pytest
        import _pytest.config

        pm = _pytest.config.get_plugin_manager()
        pm.consider_setuptools_entrypoints()
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='inspire_relations',
    version='0.0.1',
    summary='0.0.1 beta',
    url='https://github.com/inspirehep/relations',
    license='GPLv2',
    author='Eamonn Maguire',
    author_email='eamonn.maguire@cern.ch',
    description=__doc__,
    keywords='inspire relations citation graph',
    long_description="RelationManager package which connects with a neo4j graph and sends citations to be stored as a graph. "
                     "Also provides querying to get information about the references, citations, and authors related "
                     "to some record id.",
    packages=["citator"],
    zip_safe=False,
    platforms='any',

    install_requires=[
        "neomodel",
    ],
    test_suite='inspire_relations.tests',
    tests_require=test_requirements,
    cmdclass={'test': PyTest}
)
