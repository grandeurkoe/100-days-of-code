from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import INTEGER, FLOAT, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column


# The DeclarativeBase allows for the creation of new declarative bases in such a way that is compatible with
# type checkers.
class Base(DeclarativeBase):
    pass


# Create a db object using the SQLAlchemy constructor.
db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
# Configure the SQLite database, relative to app instance folder.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# Initialize the app with the extension.
db.init_app(app)


# Define db.Model
class Book(db.Model):
    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    title: Mapped[str] = mapped_column(VARCHAR(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(VARCHAR(250), nullable=False)
    rating: Mapped[str] = mapped_column(FLOAT, nullable=False)


# Create models and tables after defining them using create_all().
# with app.app_context():
#     db.create_all()

# Create A New Record.
# with app.app_context():
#     new_book = Book(title='The Name of the Wind', author='Patrick Rothfuss', rating='8.1')
#     db.session.add(new_book)
#     db.session.commit()

# Read All Records.
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title)).scalars()

# Read A Particular Record By Query.
# with app.app_context():
#     book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     print(book.title)

# Update A Particular Record By Query.
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()

#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()

# Update A Particular Record By PRIMARY KEY.
# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     #     OR
#     #     book_to_update = db.get_or_404(Book, book_id)
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit()

# Delete A Particular Record By PRIMARY KEY.
book_id = 1
with app.app_context():
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()


@app.route("/")
def home():
    return "Hello"


if __name__ == "__main__":
    # When you're running for the first time set debug to False.
    # Since flask uses a reloader it will add the same entry twice causing an Integrity Error.
    # You can set debug=True after the first run.
    app.run(debug=False)
