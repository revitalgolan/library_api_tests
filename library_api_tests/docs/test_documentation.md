
# Test Automation Documentation for Library API

## Test Coverage

### Books:
- Retrieve all books (`GET /books`)
- Add a valid book
- Attempt to add a book with missing or empty fields
- Attempt to add a book with only space at the fields value - Pay attention this test failed. Need to fix the library-management-api code to handle this case :-)
- Update an existing book
- Attempt to update a non-existent book
- Delete an existing book
- Attempt to delete a non-existent book

### Users:
- Retrieve list of registered users (`GET /users`)

### Borrowing and Returning:
- End-to-end flow: add a book → borrow it → return it
- Attempt to borrow the same book twice
- Attempt to return a book that was not borrowed
- Attempt to return a book by a different user
- Borrow a book with a non-existent user or book ID

## Why These Tests Are Important

- Ensure the system handles invalid or missing data gracefully.
- Verify full user flow from book creation to borrowing and return.
- Enforce correct business logic around borrowing and returning books.
- Prevent logic bugs that could lead to data inconsistency or system failure.
