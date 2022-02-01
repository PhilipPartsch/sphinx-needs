"""Pytest conftest module containing common test configuration and fixtures."""
import shutil

import pytest
from sphinx.testing.path import path

pytest_plugins = "sphinx.testing.fixtures"


@pytest.fixture(scope="session")
def rootdir():
    return path(__file__).parent.abspath() / "doc_test"


@pytest.fixture(scope="function")
def app(app, sphinx_test_tempdir):
    yield app

    # tear down action to clean up test tmpdir
    clean_up_tmpdir(sphinx_test_tempdir)


def copy_srcdir_to_tmpdir(srcdir, tmp):
    tmproot = tmp / srcdir
    srcdir = path(__file__).parent.abspath() / srcdir
    shutil.copytree(srcdir, tmproot)
    return tmproot


def clean_up_tmpdir(targetdir):
    shutil.rmtree(targetdir, True)