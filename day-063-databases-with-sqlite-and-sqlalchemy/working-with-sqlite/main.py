import sqlite3

# To work with SQLite database, we first need to import the sqlite3 module.

# Create a connection to a new database(if the database doesn't exist then it will be created).
db = sqlite3.connect("book-collection.db")

# Create a cursor which will control the database.
cursor = db.cursor()

# Similar to Excel files, database can contain many tables.
# Create a table in book_collection.db
# If you've already created the database.
# Comment below code out so that you don't encounter 'sqlite3.OperationalError: table books already exists' error
# cursor.execute("CREATE TABLE books( "
#                "id INTEGER PRIMARY KEY,"
#                "title varchar(250) NOT NULL UNIQUE,"
#                "author varchar(250) NOT NULL,"
#                "rating FLOAT NOT NULL)")

# Add data entry to books table.
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K. Rowling', '9.3')")
db.commit()
