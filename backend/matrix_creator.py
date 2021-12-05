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
    cursor.execute("SELECT start_dist, end_dist FROM autos_starts_and_ends_dist WHERE start_time < (%s) AND end_time > (%s)", (time_start, time_end))
    actual = cursor.fetchall()
    matrix = {}
    for i in actual:
        if i not in matrix:
            matrix[i] = 0
        matrix[i] += 1
    file = open('correspondency_matrix.csv', 'w', encoding='utf-8')


    header = []
    header.append('startCameras')
    for i in matrix:
        if i[0] not in header:
            header.append(i[0])
    w = csv.DictWriter(file, fieldnames=header)

    for i in matrix:
        row = {}
        for j in header:
            if j == 'startCameras':
                row[j] = i[0]
                continue
            cortage = (i[0], j)
            if cortage in matrix:
                row[j] = matrix[cortage]
        w.writerow(row)

    #print(actual)



start = datetime(2021, 11, 29, 18, 0)
end = datetime(2021, 11, 29, 18, 30)
get_correspondense_matrix(start, end)
# print(connection.get_dsn_parameters(), "\n")

