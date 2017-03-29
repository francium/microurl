import pprint

import MySQLdb as sqldb


class DB_Interface:
    def __init__(self):
        try:
            self.passwd = parse_passwd()
        except FileNotFoundException as fnfe:
            pass # FIXME Fail object creation (override __new__)

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def connect(self):
        self.db = sqldb.connect(db='microurl', user='microurl', passwd=self.passwd)
        self.cur = self.db.cursor()

    def close(self):
        self.db.close()

    def insert(self, micro, url, creation, expiration):
        sql = 'insert into Micros (micro_link, real_link, creation, expiration)'\
              ' values (%s, %s, %s, %s)'
        rc = self.cur.execute(sql, (micro, url, creation, expiration))
        self.db.commit()
        return rc

    def get_all(self):
        sql = 'select * from Micros'
        self.cur.execute(sql)
        return self.cur.fetchall()

    def query(self, value):
        sql = 'select * from Micros where micro_link = %s'
        self.cur.execute(sql, (value,))
        return self.cur.fetchone()


def parse_passwd():
    try:
        with open('.db_passwd', 'r') as f:
            return f.read().strip()
    except FileNotFoundException as fnfe:
        raise FileNotFoundException('No password file found (.db_passwd)')
