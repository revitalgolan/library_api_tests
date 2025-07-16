def test_get_users_success(client):
    response = client.get_users()
    assert response.status_code == 200
    assert isinstance(response.json(), list)
