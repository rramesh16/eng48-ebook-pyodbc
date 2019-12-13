from db_connect_oop import *

class EbooksBooks(MSDBConnnection):
    def __init__(self):
        super().__init__()
        self.table = 'Books'

    def __sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

    def print_all(self):
        query = "SELECT * FROM Books"
        data = self.__sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(f" ID: {record.BookID} , Title: {record.Title} , Author: {record.Author}, Published: {record.Date_Published}")

    def search_by_name(self):
            name = input('Please enter the name of the book:')
            query = f"SELECT * FROM Books WHERE Title LIKE '%{name}%'"
            result = self.__sql_query(query)
            record = result.fetchone()
            print(
                f" ID: {record.BookID} , Title: {record.Title} , Author: {record.Author}, Published: {record.Date_Published}")

    def add_book(self):
        ebook_title = input('Please enter the title of the book:')
        ebook_author = input('Please enter the name of the author:')
        ebook_published = input('Please enter the published date in the format YYYY-MM-DD')
        query = f"INSERT INTO Books(Title, Author, Date_Published) VALUES ('{ebook_title}', '{ebook_author}', '{ebook_published}')"
        result = self.cursor.execute(query)
        self.cursor.commit()
        print('All done. Thank you!')