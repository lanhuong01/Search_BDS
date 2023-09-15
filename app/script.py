import sqlite3
from models import BDS   
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()
from django.core.management import call_command

def init():
    conn = sqlite3.connect('bds.db')
    cursor = conn.cursor()
    return conn, cursor

def extract_all_data(conn, cursor, data):
    cursor.execute(f"SELECT * FROM {data}")
    return cursor.fetchall()

if __name__ == '__main__':
    conn, cursor = init()
    datas = 'data'

    data_records = extract_all_data(conn, cursor, datas)

    for record in data_records:
        bds = BDS(
            ID = record[0]
            news_type = record[1]
            price = record[2]
            size = record[3]
            direction = record[4]
            balcony_direction = record[5]
            legal = record[6]
            width = record[7]
            length = record[8]
            bedrooms = record[9]
            toilets = record[10]
            floors = record[11]
            furniture = record[12]
            url = record[13]
            location = record[14]
            description = record[15]
            range_price = record[16]
            range_size = record[17]
            city = record[18]

        )
        bds.save()

    conn.close()
