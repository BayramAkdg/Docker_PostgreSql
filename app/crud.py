import logging
import psycopg2

class BookManager:
    def __init__(self, db):
        self.db = db
        self._setup_logging()

    def _setup_logging(self):
        """Setup logging configuration."""
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        self.logger = logging.getLogger(__name__)

    def add_book(self, title, author, year, pages):
        """Add a new book to the library."""
        query = "INSERT INTO books (title, author, year, pages) VALUES (%s, %s, %s, %s)"
        values = (title, author, year, pages)

        return self._execute_query(query, values, "added")

    def get_books(self):
        """List all books in the library."""
        query = "SELECT * FROM books"

        return self._fetch_query(query)

    def update_book(self, title, new_author, new_year, new_pages):
        """Update an existing book."""
        query = """UPDATE books SET author = %s, year = %s, pages = %s WHERE title = %s"""
        values = (new_author, new_year, new_pages, title)

        return self._execute_query(query, values, "updated")

    def delete_book(self, title):
        """Delete a book from the library."""
        query = "DELETE FROM books WHERE title = %s"
        values = (title,)

        return self._execute_query(query, values, "deleted")

    def _execute_query(self, query, values, action):
        """Execute a database query."""
        try:
            self.db.cursor.execute(query, values)
            self.db.connection.commit()
            self.logger.info(f"Book successfully {action}.")
        except psycopg2.Error as e:
            self.logger.error(f"Error {action} book: {e}")

            return f"Error {action} book: {e}"

    def _fetch_query(self, query):
        """Fetch results from a database query."""
        try:
            self.db.cursor.execute(query)
            results = self.db.cursor.fetchall()
            if results:
                self.logger.info(f"Fetched {len(results)} books.")

                return results
                
            self.logger.warning("No books found.")

            return None
        except psycopg2.Error as e:
            self.logger.error(f"Error fetching books: {e}")
            
            return None
