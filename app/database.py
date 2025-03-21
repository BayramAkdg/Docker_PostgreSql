import logging
import psycopg2

class Database:
    def __init__(self, database_url="postgresql://user:password@localhost:5432/library"):
        self.connection = None
        self.cursor = None
        self.database_url = database_url
        self._setup_logging()

    def _setup_logging(self):
        """Setup logging configuration."""
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        self.logger = logging.getLogger(__name__)

    def connect(self):
        """Connect to the PostgreSQL database."""
        try:
            self.connection = psycopg2.connect(self.database_url)
            self.cursor = self.connection.cursor()
            self.logger.info("Successfully connected to the database.")
        except psycopg2.OperationalError as e:
            self.logger.error(f"Error connecting to database: {e}")
            
            raise

    def close(self):
        """Close the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            self.logger.info("Database connection closed.")
