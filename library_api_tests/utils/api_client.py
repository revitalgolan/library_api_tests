import requests
from library_api_tests.config import BASE_URL

class LibraryAPI:
    def __init__(self):
        self.base_url = BASE_URL

    def get_books(self):
        return requests.get(f"{self.base_url}/books")

    def add_book(self, book_data):
        return requests.post(f"{self.base_url}/books", json=book_data)

    def update_book(self, book_id, book_data):
        return requests.put(f"{self.base_url}/books/{book_id}", json=book_data)

    def delete_book(self, book_id):
        return requests.delete(f"{self.base_url}/books/{book_id}")

    def get_users(self):
        return requests.get(f"{self.base_url}/users")

    def borrow_book(self, user_id, book_id):
        return requests.post(f"{self.base_url}/users/{user_id}/borrow/{book_id}")

    def return_book(self, user_id, book_id):
        return requests.post(f"{self.base_url}/users/{user_id}/return/{book_id}")
