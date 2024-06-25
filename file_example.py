import requests

headers = {"Authorization": "Bearer {token}"}

with open("Gectaro-primer-importa-finance.xlsx", mode="rb") as file:
    files = {"document": file}
    data = {}
    print(
        requests.post(
            "https://api.gectaro.com/v2/companies/7323/finance/payment-operations/parse",
            headers=headers,
            files=files,
            json=data,
        ).text
    )
