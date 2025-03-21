from database import Database
from crud import BookManager
from utility import LibraryUtility

class LibraryApp:
    def __init__(self, db):
        self.db = Database()
        self.db.connect()
        self.book_manager = BookManager(self.db)
        self.utility = LibraryUtility()

    def run(self):
        """Run the Library Management System without using while loop."""
        self.utility.logger.info("Library Management System started.")
        self._process_user_choice()

    def _process_user_choice(self):
        """Process the user's choice in a recursive manner."""
        choice = self.utility.show_menu()
        if choice == "5":
            self.utility._exit(self.book_manager)
            self.db.close()
        else:
            self.utility.handle_choice(choice, self.book_manager)
            self._process_user_choice()

if __name__ == "__main__":
    app = LibraryApp()
    app.run()
