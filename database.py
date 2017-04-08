import hashlib
import json
import sys

from Crypto.Hash import SHA256
import MySQLdb as sqldb


class DB_Interface:
    def __init__(self):
        try:
            config = parse_config()
            self.user = config['user']
            self.passwd = config['password']
            self.host = config['host']
            self.db_name = config['db_name']
        except FileNotFoundError as fnfe:
            pass # FIXME Fail object creation (override __new__)

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def connect(self):
        self.db = sqldb.connect(db=self.db_name, user=self.user,
                host=self.host, passwd=self.passwd)
        self.cur = self.db.cursor()

    def close(self):
        self.db.close()

    def create(self):
        sql = read_schema()
        rc = self.cur.execute(sql)
        return rc

    def clear(self):
        sql = 'delete from Micros'
        rc = self.cur.execute(sql)
        return rc

    def insert(self, micro, url, creation, expiration, public):
        sql = 'insert into Micros (id, micro_link, real_link, creation, expiration, public)'\
              ' values (%s, %s, %s, %s, %s, %s)'

        id = SHA256.new(url.encode('latin1')).hexdigest()
        rc = self.cur.execute(sql, (id, micro, url, creation, expiration, public))
        self.db.commit()
        return rc

    def get_all(self):
        sql = 'select * from Micros'
        self.cur.execute(sql)
        return self.cur.fetchall()

    def get_top(self):
        sql = '''select *
                 from Micros
                 where public = 1
                 order by hits desc'''
        self.cur.execute(sql)
        return self.cur.fetchall()

    def query(self, value):
        sql = 'select * from Micros where micro_link = %s'
        self.cur.execute(sql, (value,))
        return self.cur.fetchone()


def parse_config():
    with open('.config.json', 'r') as f:
        return json.loads(f.read())


def read_schema():
    with open('schema.sql', 'r') as f:
        return f.read()


def yesno(msg):
    return input(msg).lower() in ('yes', 'y')


def create_database():
    with DB_Interface() as db:
        db.create()


def clear_database():
    if yesno('Clear database? Are you sure? '):
        with DB_Interface() as db:
            db.clear()

        print('Database cleared.')


if __name__ == '__main__':
    if (len(sys.argv) > 1):
        if sys.argv[1] == 'create':
            sys.exit(create_database())
        elif sys.argv[1] == 'clear':
            sys.exit(clear_database())
        else:
            print('{}: unknown command'.format(sys.argv[0]))
