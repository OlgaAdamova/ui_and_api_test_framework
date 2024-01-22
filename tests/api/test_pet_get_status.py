import requests


def test_get_pet_by_status():
    for status in ("available", "pending", "sold"):
        response = requests.get(
            url="https://petstore.swagger.io/v2/pet/findByStatus?",
            params={"status": status},
        )
        status1 = "available"
        status2 = "pending"
        status3 = "sold"
        assert status1 == "available" and status2 == "pending" and status3 == "sold"

        assert response.status_code == 200

        pet_list = response.json()
        assert len(pet_list) > 0
