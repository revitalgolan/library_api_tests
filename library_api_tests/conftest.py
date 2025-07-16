import pytest
from library_api_tests.utils.api_client import LibraryAPI

@pytest.fixture(scope="module")
def client():
    return LibraryAPI()