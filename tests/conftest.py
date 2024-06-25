from datetime import datetime

import pytest

from tests.gectaro_http_client import GectaroHttpClient


def pytest_addoption(parser):
    parser.addoption("--token", help="token for test API")
    parser.addoption(
        "--url", default="https://api.gectaro.com", help="base url for API client"
    )


@pytest.fixture(scope="session")
def token(request):
    return request.config.getoption("--token")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def client(token, url):
    client = GectaroHttpClient(base_url=url, token=token)
    yield client
    # teardown


@pytest.fixture
def resource(client):
    data = {
        "name": "first_resource",
        "needed_at": int(datetime.now().timestamp()),
        "project_id": 80024,
        "type": 1,
        "volume": 5,
    }

    resource_id = client.post_projects_resources(data=data).json()["id"]

    yield resource_id

    # todo: delete resource


@pytest.fixture
def is_over_budget(request):
    return int(request.param)
