import json

def main():
    try:
        with open("book_log.json", "r", encoding="utf-8") as file:
            books = json.load(file)
    except FileNotFoundError:
        books = []

    print("=== 読書記録 ===\n1. 本を登録\n2. 登録した本を一覧表示\n3. 本を検索\n4. 終了")
    
    while True:
        option = input("選択：")

        if option == "1" or option == "１":
            book_name = input("書名：")
            if book_name == "":
                continue
            author_name = input("著者：")
            if author_name == "":
                continue
            book = {
                "book": book_name,
                "author": author_name
            }
            books.append(book)
            with open("book_log.json", "w", encoding= "utf-8") as file:
                json.dump(books, file, ensure_ascii= False, indent= 4)
            print("登録しました。")
            continue

        if option == "2" or option == "２":
            for number, book  in enumerate(books, start=1):
                print(f"{number}.{book['book']}/{book['author']}")
            continue


        if option == "3" or option == "３":
            keyword = input("検索する書名：")
            found = False

            for book in books:
                if keyword in book["book"]:
                    print(f"{book['book']} / {book['author']}")
                    found = True
            if not found:
                print("該当する本はありません。")
            continue


        if option == "4" or option == "４":
            break

        else:
            print("1~4で選択してください。")
            continue

if __name__ == "__main__":
    main()