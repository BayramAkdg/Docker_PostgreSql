from crud import BookManager
from utility import get_int_input

def main():
    manager = BookManager()

    while True:
        print("\n1. Kitap Ekle")
        print("2. Kitapları Listele")
        print("3. Kitap Güncelle")
        print("4. Kitap Sil")
        print("5. Çıkış")

        choice = input("Seçiminiz: ").strip()

        if choice == "1":
            kitap_adi = input("Kitap adı: ")
            yazar = input("Yazar: ")
            yayin_yili = get_int_input("Yayın yılı: ")
            sayfa_sayisi = get_int_input("Sayfa sayısı: ")
            manager.add_book(kitap_adi, yazar, yayin_yili, sayfa_sayisi)

        elif choice == "2":
            manager.list_books()

        elif choice == "3":
            book_id = get_int_input("Güncellenecek kitap ID: ")
            yeni_yazar = input("Yeni yazar: ")
            yeni_yayin_yili = get_int_input("Yeni yayın yılı: ")
            yeni_sayfa_sayisi = get_int_input("Yeni sayfa sayısı: ")
            manager.update_book(book_id, yeni_yazar, yeni_yayin_yili, yeni_sayfa_sayisi)

        elif choice == "4":
            book_id = get_int_input("Silinecek kitap ID: ")
            manager.delete_book(book_id)

        elif choice == "5":
            print("Çıkış yapılıyor...")
            manager.close()
            break

        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    main()
