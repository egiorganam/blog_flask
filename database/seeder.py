import sqlite3 as sql

DB_PATH = '/Users/ixmx3107/PycharmProjects/blog-flask/database/miniblog.db'


def create_db():
    connection = sql.connect(DB_PATH)
    connection.commit()
    connection.close()


if __name__ == '__main__':
    create_db()
