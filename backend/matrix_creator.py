import csv

import psycopg2
from datetime import datetime

connection = psycopg2.connect(user="rouser",
                                  password="Pass1234",
                                  host="rc1c-90mkmxvku0h105em.mdb.yandexcloud.net",
                                  port="6432",
                                  database="db1")
cursor = connection.cursor()

def get_correspondense_matrix(time_start, time_end):
    cursor.execute("SELECT start_cam, end_cam FROM autos_starts_and_ends WHERE start_time < (%s) AND end_time > (%s)", (time_start, time_end))
    actual = cursor.fetchall()
    matrix = {}
    for i in actual:
        if i not in matrix:
            matrix[i] = 0
        matrix[i] += 1
    file = open('correspondency_ matrix.csv', 'w')

    header = []
    header.append('startCameras')
    for i in matrix:
        header.append(i[0])
    w = csv.DictWriter(file, fieldnames=header)

    for i in matrix:
        row = {}
        row['startCameras'] = i[1]
        for j in header:
            row[j] = matrix[i]
        w.writerow(row)

    print(actual)



start = datetime(2021, 11, 29, 18, 0)
end = datetime(2021, 11, 29, 18, 30)
get_correspondense_matrix(start, end)
# print(connection.get_dsn_parameters(), "\n")

