import sqlite3 as sl

# создание подключения
connect = sl.connect('sharp.db')


def createDB():
    """
    Создание таблицы в БД
    :return:
    """
    with connect:
        connect.execute("""
            CREATE TABLE USER (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
                );
        """)


def insertDataInDB():
    """
    Наполнение созданной таблицы данными
    :return:
    """
    sql = 'INSERT INTO USER (id, name, age) values(?,?,?)'
    data = [
        (4, "I", 12),
        (5, "understand", 22),
        (6, "this", 33)
    ]
    with connect:
        connect.executemany(sql, data)


def outoutData():
    """
    Вывод данных с помощью запроса
    :return:
    """
    with connect:
        data = connect.execute("SELECT * FROM USER")
        for row in data:
            print(row)


if __name__ == '__main__':
    createDB()
    insertDataInDB()
    outoutData()
