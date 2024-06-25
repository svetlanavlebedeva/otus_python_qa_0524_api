from typing import Union

import requests

from response_models import ProjectTaskRequestBody


class GectaroHttpClient:

    def __init__(self, base_url, token, project_id="80024"):
        self.session = requests.Session()
        self.session.headers["Authorization"] = f"Bearer {token}"
        self.base_url = base_url
        self.project_id = project_id

    def get_projects_resource_requests(self):
        response = self.session.get(
            f"{self.base_url}/v1/projects/" f"{self.project_id}/resource-requests"
        )
        return response

    def post_projects_resources(self, data: dict):
        response = self.session.post(
            f"{self.base_url}/v1/projects/" f"{self.project_id}/resources", json=data
        )
        return response

    def post_projects_resource_requests(
        self, data: Union[dict, ProjectTaskRequestBody]
    ):
        # data может быть либо dict, либо моделью ProjectTaskRequestBody
        response = self.session.post(
            f"{self.base_url}/v1/projects/" f"{self.project_id}/resource-requests",
            # если data - это dict, не меняем,
            # а если модель - то конвертируем в словарь
            # с помощью .model_dump()
            json=data if isinstance(data, dict) else data.model_dump(),
        )

        return response
