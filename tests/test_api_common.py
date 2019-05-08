import json


def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data.decode())
    assert data['hello'] == "world"
