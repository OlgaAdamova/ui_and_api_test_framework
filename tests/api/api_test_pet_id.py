import requests

def test_api_jokes():
    START_ID = 100
    END_ID = 215
    AMOUNT = 9
    CATEGORY = "Dark"

    response = requests.get(
        url=f"https://v2.jokeapi.dev/joke/{CATEGORY}",
        params={
            f"idRange": f"{START_ID}-{END_ID}",
            "amount": AMOUNT,
            "type": "single",
        },
    )

    assert response.status_code == 200

    json_data = response.json()

    error_value = json_data["error"]
    assert error_value is False, f"error key in json is actually {error_value}"

    amount_of_jokes = json_data["amount"]
    assert amount_of_jokes == AMOUNT

    joke_list = json_data["jokes"]

    for joke in joke_list:
        joke_id = joke["id"]
        assert START_ID <= joke_id <= END_ID, f"Joke id {joke_id} is not in range {START_ID}-{END_ID}"

        joke_text = joke["joke"]
        assert len(joke_text) > 0, f"Length of joke id {joke_text} is 0"

        joke_category = joke["category"]
        assert joke_category == CATEGORY, f'Joke category is {joke_category}'






























