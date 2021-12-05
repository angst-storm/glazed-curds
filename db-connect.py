import psycopg2
import json

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


def cameras2json():
    cur.execute('SELECT * FROM not_active_cameras')
    cameras = []
    for camera in cur.fetchall():
        cameras.append({'name': camera[0], 'lat': float(camera[1]), 'lng': float(camera[2])})
    json.dump(cameras, open("cameras.json", "w", encoding="utf-8"), ensure_ascii=False)
