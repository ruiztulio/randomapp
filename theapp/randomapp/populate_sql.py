#!/usr/bin/env python3

from faker import Faker
import os
import sys
import psycopg2


def generate_values(n_values):
    res = []
    fakengen = Faker()
    while len(res) < n_values:
        res.append((
            fakengen.first_name(),
            fakengen.last_name(),
            fakengen.email()
        ))
    return res


def insert_values(n_values):
    conn = psycopg2.connect(dbname=os.getenv('DB_NAME'),
                            user=os.getenv('DB_USER'),
                            password=os.getenv('DB_PASSWORD'),
                            host=os.getenv('DB_HOST'))
    cur = conn.cursor()
    values =  generate_values(n_values)
    args_str = b','.join(cur.mogrify("(%s,%s,%s)", record) for record in values) 
    cur.execute(b'INSERT INTO origin (first_name, last_name, email) VALUES ' + args_str)
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError('Invalid parameter count')
    insert_values(int(sys.argv[1]))