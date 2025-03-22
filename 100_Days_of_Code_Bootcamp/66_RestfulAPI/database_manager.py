import sqlite3
import random


class DatabaseManager:

    def __init__(self):

        self.all_cafes = []
        self.db = sqlite3.connect("cafes.db")
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT id, name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats, coffee_price FROM cafe;")
        self.dataTuples = self.cursor.fetchall()
        self.read_cafes_from_database()

    def read_cafes_from_database(self):

        print("All cafes read from database")

        for self.cafeTuple in self.dataTuples:
            self.entry = {
                "id": self.cafeTuple[0],
                "name": self.cafeTuple[1],
                "map_url": self.cafeTuple[2],
                "img_url": self.cafeTuple[3],
                "location": self.cafeTuple[4],
                "has_sockets": self.cafeTuple[5],
                "has_toilet": self.cafeTuple[6],
                "has_wifi": self.cafeTuple[7],
                "can_take_calls": self.cafeTuple[8],
                "seats": self.cafeTuple[9],
                "coffee_price": self.cafeTuple[10],
            }
            self.all_cafes.append(self.entry)

    def get_random_cafe(self):
        return random.choice(self.all_cafes)

    def get_all_cafes(self):
        print(self.all_cafes)
        self.cafe_dict = {}

        self.counter = 0

        for cafe in self.all_cafes:
            self.cafe_dict[str(cafe["id"])] = cafe
            self.counter += 1

        return self.cafe_dict
