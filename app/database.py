import psycopg2
import os
import logging

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self._setup_logging()

    def _setup_logging(self):
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        self.logger = logging.getLogger(__name__)

    def connect(self):
        """Connect to the PostgreSQL database."""
        
        try:
            database_url = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/library")
            self.connection = psycopg2.connect(database_url)
            self.cursor = self.connection.cursor()
            self.logger.info("Connected to the PostgreSQL database.")
            
        except psycopg2.Error as e:
            self.logger.error(f"Error connecting to database: {e}")

    def close(self):
        """Close the database connection."""
        
        if self.cursor:
            self.cursor.close()
            
        if self.connection:
            self.connection.close()
            self.logger.info("Database connection closed.")
