import csv
import json

import psycopg2
from datetime import datetime

connection = psycopg2.connect(user="rouser",
                                  password="Pass1234",
                                  host="rc1c-90mkmxvku0h105em.mdb.yandexcloud.net",
                                  port="6432",
                                  database="db1")
cursor = connection.cursor()

def get_correspondense_matrix(time_start, time_end):
    cursor.execute("SELECT start_dist, end_dist FROM autos_starts_and_ends_dist WHERE start_time < (%s) AND end_time > (%s)", (time_end, time_start))
    actual = cursor.fetchall()
    matrix = {}
    for i in actual:
        if i not in matrix:
            matrix[i] = 0
        matrix[i] += 1
    file = open('correspondency_matrix.json', 'w', encoding='utf-8')

    # настраиваемое значение
    max_val = (time_end - time_start).total_seconds() / 60

    out_matrix = []
    for rel in matrix:
        if rel[0] != rel[1]:
            value = abs(matrix[rel] / max_val if matrix[rel] / max_val <= 10 else 10)
            out_matrix.append({'dispatch': rel[0], 'arrival': rel[1], 'value': value})

    json.dump(out_matrix, file, indent=4, ensure_ascii=False)



start = datetime(2021, 11, 29, 18, 0)
end = datetime(2021, 11, 29, 18, 10)
get_correspondense_matrix(start, end)
# print(connection.get_dsn_parameters(), "\n")

