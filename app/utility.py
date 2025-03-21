import logging

class LibraryUtility:
    def __init__(self):
        self._setup_logging()

    def _setup_logging(self):
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        self.logger = logging.getLogger(__name__)

    def show_menu(self):
        """Display the Library Management System menu."""
        self.logger.info("Displaying the menu.")
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")
        
        return input("Your choice: ").strip()

    def handle_choice(self, choice, book_manager):
        """Handle user's choice from the menu."""
        if choice == "1":
            title = input("Book title: ").strip()
            author = input("Author: ").strip()
            
            try:
                year = int(input("Year: ").strip())
                pages = int(input("Page count: ").strip())
            except ValueError:
                self.logger.error("Invalid input for year or pages. Please enter valid integers.")
                print("Invalid input for year or pages. Please enter valid integers.")
                
                return

            result = book_manager.add_book(title, author, year, pages)
            self.logger.info(f"Add Book result: {result}")
            print(result)

        elif choice == "2":
            books = book_manager.get_books()
            if isinstance(books, list) and books:
                self.logger.info(f"Listing {len(books)} books.")
                print("\nBooks in the Library:")
                
                for book in books:
                    print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, Pages: {book[4]}")
                    
            else:
                self.logger.warning("No books found.")
                print(books)

        elif choice == "3":
            book_id = input("Book ID to update: ").strip()
            new_author = input("New author: ").strip()
            
            try:
                new_year = int(input("New year: ").strip())
                new_pages = int(input("New page count: ").strip())
            except ValueError:
                self.logger.error("Invalid input for year or pages. Please enter valid integers.")
                print("Invalid input for year or pages. Please enter valid integers.")
                
                return

            result = book_manager.update_book(book_id, new_author, new_year, new_pages)
            self.logger.info(f"Update Book result: {result}")
            print(result)

        elif choice == "4":
            book_id = input("Book ID to delete: ").strip()
            result = book_manager.delete_book(book_id)
            self.logger.info(f"Delete Book result: {result}")
            print(result)
        elif choice == "5":
            self.logger.info("Exiting the system...")
            print("Exiting the system...")
        else:
            self.logger.error("Invalid choice, please try again.")
            print("Invalid choice, please try again.")
