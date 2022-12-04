import json


book = {
    "Title": "The Last Wish",
    "Author": "A. Sapkowski",
    "Genre": "Fantasy",
    "YearOfRelease": 1990,
    "NumOfPages": 350
    }

with open("favourite.json","w") as file:
    json.dump(book, file, indent=4)