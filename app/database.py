import psycopg2

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="library_db",
            user="postgres",
            password="postgres",
            host="db",
            port="5432"
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            kitap_adi TEXT NOT NULL,
            yazar TEXT NOT NULL,
            yayin_yili INTEGER,
            sayfa_sayisi INTEGER
        );
        """
        self.cursor.execute(query)
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
