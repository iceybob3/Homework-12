import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')

# pd.options.display.max_columns = 10
authors = pd.read_sql("""SELECT last FROM authors ORDER BY last DESC""", connection)
print(authors)
print()

titles = pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection)
print(titles)
print()

wald = pd.read_sql("""SELECT title, copyright, isbn FROM authors INNER JOIN titles
                    WHERE last LIKE 'W%' ORDER BY title  ASC""", connection)
print(wald)
print()

cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last, id) VALUES ('Sue', 'Red', '6')""")

authors = pd.read_sql("""SELECT last FROM authors ORDER BY last DESC""", connection)
print(authors)

cursor = cursor.execute("""INSERT INTO author_ISBN (id, isbn) VALUES ('6', '0385934517')""")
cursor = cursor.execute("""INSERT INTO titles (isbn, title, edition, copyright) 
                           VALUES ('0385934517', 'New Book', '1', '2023')""")

all_ISBN = pd.read_sql("""SELECT * FROM author_ISBN""", connection)
print(all_ISBN)

all_author = pd.read_sql("""SELECT * FROM authors""", connection)
print(all_author)

all_title = pd.read_sql("""SELECT * FROM titles""", connection)
print(all_title)
