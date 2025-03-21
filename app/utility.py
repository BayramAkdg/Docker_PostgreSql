import logging

class LibraryUtility:
    def __init__(self):
        self._setup_logging()

    def _setup_logging(self):
        """Setup logging configuration."""
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        self.logger = logging.getLogger(__name__)

    def show_menu(self):
        """Display the Library Management System menu."""
        self.logger.info("Displaying menu.")
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")

        return input("Your choice: ").strip()

    def handle_choice(self, choice, book_manager):
        """Handle user's choice from the menu."""
        actions = {
            "1": self._add_book,
            "2": self._list_books,
            "3": self._update_book,
            "4": self._delete_book,
            "5": self._exit
        }

        action = actions.get(choice)
        if action:
            action(book_manager)
        else:
            self.logger.warning("Invalid choice, please try again.")

    def _add_book(self, book_manager):
        """Handle the add book action."""
        title, author, year, pages = self._get_book_details()
        if title and author:
            book_manager.add_book(title, author, year, pages)

    def _list_books(self, book_manager):
        """Handle the list books action."""
        books = book_manager.get_books()
        if books:
            self._display_books(books)

    def _update_book(self, book_manager):
        """Handle the update book action."""
        title = input("Enter book title to update: ").strip()
        new_author, new_year, new_pages = self._get_book_details()
        book_manager.update_book(title, new_author, new_year, new_pages)

    def _delete_book(self, book_manager):
        """Handle the delete book action."""
        title = input("Enter book title to delete: ").strip()
        book_manager.delete_book(title)

    def _exit(self, book_manager):
        """Handle the exit action."""
        self.logger.info("Exiting the system.")

    def _get_book_details(self):
        """Get book details from user input."""
        title = input("Book title: ").strip()
        author = input("Author: ").strip()
        
        try:
            year = int(input("Year: ").strip())
            pages = int(input("Page count: ").strip())

            return title, author, year, pages
        except ValueError:
            self.logger.warning("Invalid input for year or page count. Please enter valid integers.")

            return None, None, None, None

    def _display_books(self, books):
        """Display list of books."""
        print("\nBooks in the Library:")
        
        for idx, book in enumerate(books, start=1):
            print(f"ID: {idx}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, Pages: {book[4]}")
