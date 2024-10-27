import pytest
from flask import url_for
from application import application

@pytest.fixture
def client():
    with application.app_context():
        yield application.test_client()

def test_pred_route(client):
    test_sentences = [
        ['This is a fake news', 0],
        ['This is a true news', 1],
        ['This is a news about coronavirus', 1],  # This should be predicted as REAL (1)
        ['Sponge bob has arrived', 0],
        ['Biden has arrived', 1],
    ]
    for sentence in test_sentences:
        # Send a GET request to the /pred route with a sentence
        response = client.get(f"/pred?sentence={sentence[0]}")
        # print(f"sentence is {sentence[0]}")
        # print(f"response is {response.get_data(as_text=True)}")

        # Assert that the response status code is 200
        assert response.status_code == 200

        # Assert that the response contains the expected prediction (0 for FAKE)
        assert response.get_data(as_text=True) == str(sentence[1])

