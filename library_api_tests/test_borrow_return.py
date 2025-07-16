def test_borrow_and_return_flow(client):
    book_data = {"title": "Full Flow", "author": "Flow Tester"}
    book_id = client.add_book(book_data).json()["id"]
    user_id = 1

    borrow_resp = client.borrow_book(user_id, book_id)
    assert borrow_resp.status_code == 200

    return_resp = client.return_book(user_id, book_id)
    assert return_resp.status_code == 200

def test_double_borrow_attempt(client):
    book_data = {"title": "Double Borrow", "author": "Author"}
    book_id = client.add_book(book_data).json()["id"]
    user_id = 1

    client.borrow_book(user_id, book_id)
    second_borrow = client.borrow_book(user_id, book_id)
    assert second_borrow.status_code == 400

def test_return_unborrowed_book(client):
    book_data = {"title": "Never Borrowed", "author": "Nobody"}
    book_id = client.add_book(book_data).json()["id"]
    response = client.return_book(1, book_id)
    assert response.status_code == 400

def test_borrow_return_wrong_user(client):
    book_data = {"title": "Wrong User Flow", "author": "Someone"}
    book_id = client.add_book(book_data).json()["id"]
    client.borrow_book(1, book_id)
    response = client.return_book(2, book_id)
    assert response.status_code == 400

def test_borrow_with_invalid_user(client):
    book_data = {"title": "Borrow Invalid User", "author": "Test"}
    book_id = client.add_book(book_data).json()["id"]
    response = client.borrow_book(999, book_id)
    assert response.status_code == 404

def test_borrow_with_invalid_book(client):
    response = client.borrow_book(1, 999999)
    assert response.status_code == 404
