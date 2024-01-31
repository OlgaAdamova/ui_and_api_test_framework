import requests


URL = "http://127.0.0.1:5000"
FIRST_NAME = "Denis "
LAST_NAME = "Ivanov"
EMAIL = "d@gmail.com"


def test_create_and_fetch_users():
    url = URL
    request_payload = {
        "first_name": FIRST_NAME,
        "last_name": LAST_NAME,
        "email": EMAIL
    }

    response_post = requests.post(f"{URL}/users/", json=request_payload)
    response_payload = response_post.json()

    assert response_payload["first_name"] == FIRST_NAME
    assert response_payload["last_name"] == LAST_NAME
    assert response_payload["email"] == EMAIL
    assert response_payload["id"] > 0
    user_id = response_payload["id"]

    print(response_post.json())

    response_get = requests.get(
        url=f"{URL}/users/{user_id}",
    )

    print(response_get.json())
    assert response_get.status_code == 200
    assert response_payload["first_name"] == FIRST_NAME
    assert response_payload["last_name"] == LAST_NAME
    assert response_payload["email"] == EMAIL
    assert response_payload["id"] == user_id




