from datetime import datetime

from gectaro_http_client import GectaroHttpClient


def test_get_resource_requests(token, url):
    client = GectaroHttpClient(base_url=url,
                               token=token)
    response = client.get_projects_resource_requests()
    assert response.status_code == 200
    assert response.json()
    for item in response.json():
        assert item["id"] is not None
        assert item["volume"]


def test_post_resource_requests(token, url):
    client = GectaroHttpClient(base_url=url,
                               token=token)
    data = {'name': 'first_resource',
            'needed_at': datetime.now().timestamp(),
            'project_id': 80024,
            'type': 1,
            'volume': 5}

    resource_id = client.post_projects_resources(data=data).json()['id']

    data = {"project_tasks_resource_id": resource_id,
            "volume": 10,
            "cost": 5,
            "needed_at": datetime.now().timestamp(),
            "is_over_budget": 1}

    response = client.post_projects_resource_requests(data=data)
    assert response.status_code == 201
