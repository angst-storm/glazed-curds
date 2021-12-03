import psycopg2

db = psycopg2.connect("""
    host=rc1c-90mkmxvku0h105em.mdb.yandexcloud.net 
    port=6432
    sslmode=verify-full
    dbname=db1
    user=rouser
    password=Pass1234
    target_session_attrs=read-write
""")
cur = db.cursor()


def tables_data():
    cur.execute('SELECT * FROM INFORMATION_SCHEMA.TABLES')
    for table in cur.fetchall():
        print(table[2])


def photo_detection():
    cur.execute('SELECT * FROM views')
    print(len(cur.fetchall()))
    print(cur.fetchone())


def radio_detection_coordinates():
    cur.execute('SELECT * FROM det_coords')
    print(len(cur.fetchall()))
    print(cur.fetchone())


def radio_detection_data():
    cur.execute('SELECT * FROM detectors')
    print(len(cur.fetchall()))
    print(cur.fetchone())


def sensors():
    cur.execute('SELECT * FROM sensors')
    print(len(cur.fetchall()))
    print(cur.fetchone())
