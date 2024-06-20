import pytest


def pytest_addoption(parser):
    parser.addoption("--token",
                     help="token for test API")
    parser.addoption("--url",
                     default="https://api.gectaro.com",
                     help="base url for API client")


@pytest.fixture(scope="session")
def token(request):
    return request.config.getoption("--token")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")
