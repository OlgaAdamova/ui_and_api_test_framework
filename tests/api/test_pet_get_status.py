import requests


def test_get_pet_by_status():
    for status in ("available", "pending", "sold"):
        response = requests.get(
            url="https://petstore.swagger.io/v2/pet/findByStatus?",
            params={"status": status},
        )

        assert response.status_code == 200

        pet_list = response.json()
        assert len(pet_list) > 0

        for pet in pet_list:
            assert pet["status"] == status

