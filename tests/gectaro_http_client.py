import requests


class GectaroHttpClient:

    def __init__(self, base_url, token, project_id="80024"):
        self.session = requests.Session()
        self.session.headers["Authorization"] = f"Bearer {token}"
        self.base_url = base_url
        self.project_id = project_id

    def get_projects_resource_requests(self):
        response = self.session.get(f'{self.base_url}/v1/projects/'
                                    f'{self.project_id}/resource-requests')
        return response

    def post_projects_resources(self, data):
        response = self.session.post(f"{self.base_url}/v1/projects/"
                                     f"{self.project_id}/resources",
                                     json=data)
        return response

    def post_projects_resource_requests(self, data):
        response = self.session.post(f"{self.base_url}/v1/projects/"
                                     f"{self.project_id}/resource-requests",
                                     json=data)
        return response
