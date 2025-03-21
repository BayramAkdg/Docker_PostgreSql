from database import Database

class BookManager:
    def __init__(self):
        self.db = Database()

    def add_book(self, kitap_adi, yazar, yayin_yili, sayfa_sayisi):
        query = "INSERT INTO books (kitap_adi, yazar, yayin_yili, sayfa_sayisi) VALUES (%s, %s, %s, %s)"
        self.db.cursor.execute(query, (kitap_adi, yazar, yayin_yili, sayfa_sayisi))
        self.db.conn.commit()
        print("Kitap başarıyla eklendi!")

    def list_books(self):
        query = "SELECT * FROM books"
        self.db.cursor.execute(query)
        books = self.db.cursor.fetchall()
        
        if not books:
            print("Kütüphane boş!")
        else:
            for book in books:
                print(f"ID: {book[0]}, Kitap Adı: {book[1]}, Yazar: {book[2]}, Yayın Yılı: {book[3]}, Sayfa Sayısı: {book[4]}")

    def update_book(self, book_id, yeni_yazar, yeni_yayin_yili, yeni_sayfa_sayisi):
        query = "UPDATE books SET yazar=%s, yayin_yili=%s, sayfa_sayisi=%s WHERE id=%s"
        self.db.cursor.execute(query, (yeni_yazar, yeni_yayin_yili, yeni_sayfa_sayisi, book_id))
        self.db.conn.commit()
        print("Kitap başarıyla güncellendi!")

    def delete_book(self, book_id):
        query = "DELETE FROM books WHERE id=%s"
        self.db.cursor.execute(query, (book_id,))
        self.db.conn.commit()
        print("Kitap başarıyla silindi!")

    def close(self):
        self.db.close_connection()
