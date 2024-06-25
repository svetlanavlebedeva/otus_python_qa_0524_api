from datetime import datetime

import pytest

from response_models import ResourceRequestResponse, ProjectTaskRequestBody


def test_get_resource_requests(client):
    response = client.get_projects_resource_requests()
    assert response.status_code == 200
    ResourceRequestResponse(project_tasks=response.json())


@pytest.mark.parametrize("is_over_budget", [False, True], indirect=True, ids=['Test with False',
                                                                              'Test with True'])
def test_post_resource_requests(client, resource, is_over_budget):
    data = ProjectTaskRequestBody(
        project_tasks_resource_id=resource,
        volume="5",
        cost="5",
        is_over_budget=False,
        needed_at=int(datetime.now().timestamp()),
    )

    response = client.post_projects_resource_requests(data=data)
    assert response.status_code == 201
