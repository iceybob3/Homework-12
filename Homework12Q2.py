import sqlite3

connection = sqlite3.connect('books.db')
cursor = connection.cursor()

info = cursor.execute("""SELECT * FROM titles""")

for i in range(0, 4):
    print(info.description[i][0], end=' ')
    if i == 0:
        print(end='        ')
    elif i == 1:
        print(end='                             ')
    elif i == 2:
        print(end='    ')
print()

for entry in info.fetchall():
    for i in range(0, 4):
        print(entry[i], end='   ')
        maxSize = 32
        size = len(str(entry[i]))
        if i == 1:
            if size < maxSize:
                for j in range(size, maxSize):
                    print(end=' ')
        if i == 2:
            if len(str(entry[i])) == 1:
                print(end='        ')
            else:
                print(end='       ')

    print()
