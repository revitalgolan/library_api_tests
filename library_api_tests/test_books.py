def test_get_books_success(client):
    response = client.get_books()
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_book_success(client):
    book_data = {"title": "Valid Book", "author": "Test Author"}
    response = client.add_book(book_data)
    assert response.status_code == 201

def test_add_book_missing_title(client):
    book_data = {"author": "Author Only"}
    response = client.add_book(book_data)
    assert response.status_code == 400

def test_add_book_empty_title(client):
    book_data = {"title": "", "author": "Author"}
    response = client.add_book(book_data)
    assert response.status_code == 400

def test_add_book_space_title(client):
    book_data = {"title": " ", "author": "Author"}
    response = client.add_book(book_data)
    assert response.status_code == 400

def test_add_book_missing_author(client):
    book_data = {"title": "Title Only"}
    response = client.add_book(book_data)
    assert response.status_code == 400

def test_add_book_empty_author(client):
    book_data = {"title": "Title", "author": ""}
    response = client.add_book(book_data)
    assert response.status_code == 400

def test_add_book_space_author(client):
    book_data = {"title": "Title", "author": " "}
    response = client.add_book(book_data)
    assert response.status_code == 400

def test_update_book_success(client):
    book_data = {"title": "To Update", "author": "Updator"}
    book_id = client.add_book(book_data).json()["id"]
    response = client.update_book(book_id, {"title": "Updated Title"})
    assert response.status_code == 200

def test_update_book_not_found(client):
    response = client.update_book(999999, {"title": "Ghost"})
    assert response.status_code == 404

def test_delete_book_success(client):
    book_data = {"title": "To Delete", "author": "Deleter"}
    book_id = client.add_book(book_data).json()["id"]
    response = client.delete_book(book_id)
    assert response.status_code == 200

def test_delete_book_not_found(client):
    response = client.delete_book(999999)
    assert response.status_code == 404
