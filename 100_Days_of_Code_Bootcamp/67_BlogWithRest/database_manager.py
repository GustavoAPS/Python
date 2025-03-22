from flask import Flask, render_template, request, redirect, url_for
import sqlite3


# crud - CREATE READ UPDATE DELETE


class DatabaseManager:

    def __init__(self):
        print("database initialized")

        self.db = sqlite3.connect("posts.db", check_same_thread=False)
        self.cursor = self.db.cursor()
        self.create_database()
        self.all_posts = []

    def create_database(self):

        self.cursor.execute("CREATE TABLE IF NOT EXISTS posts "
                            "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
                            "title varchar(250) NOT NULL UNIQUE, "
                            "sub_title varchar(250) NOT NULL,  "
                            "post_text text NOT NULL)")

        self.db.commit()

    def create_new_post(self, post_title, post_sub_title, post_text):
        self.cursor.execute(f"INSERT OR REPLACE INTO posts "
                            "(title,sub_title,post_text)"
                            f"VALUES('{post_title}','{post_sub_title}','{post_text}')")
        self.db.commit()

    def get_all_posts(self):

        print("Get all posts called")

        self.cursor.execute("SELECT id, title, sub_title, post_text FROM posts;")

        for self.post_tuple in self.cursor.fetchall():
            print("-----")
            self.entry={
                "id": self.post_tuple[0],
                "title": self.post_tuple[1],
                "sub_title": self.post_tuple[2],
                "text": self.post_tuple[3],
            }
            self.all_posts.append(self.entry)

        return self.all_posts


    # dataTuples = cursor.fetchall()

    # all_books = []

    # for bookTuple in dataTuples:
    #    entry = {
    #        "title": bookTuple[0],
    #        "author": bookTuple[1],
    #        "rating": bookTuple[2],
    #    }
    #    all_books.append(entry)

    def get_post(self):
        pass

    def update_post(self):
        pass

    def delete_post(self):
        pass

# cursor.execute("INSERT OR REPLACE INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# cursor.execute("INSERT OR REPLACE INTO books VALUES(2, 'The Hobbit', 'J. R. R. Tolkien', '9.75')")
# cursor.execute("INSERT OR REPLACE INTO books VALUES(3, 'Percy Jackson & the Olympians: The Lightning Thief', 'Rick Riordan', '8.5')")


# cursor.execute("SELECT title, author, rating FROM books;")
# dataTuples = cursor.fetchall()

# all_books = []

# for bookTuple in dataTuples:
#    entry = {
#        "title": bookTuple[0],
#        "author": bookTuple[1],
#        "rating": bookTuple[2],
#    }
#    all_books.append(entry)

# db.commit()

# print(all_books)
