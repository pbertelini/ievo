# -*- coding: utf-8 -*-

import sys
import sqlite3

import libs.ana_class_atest_log as log


import configparser
config = configparser.RawConfigParser(allow_no_value=True)
config.read('./conf/ana_class_atest.cfg')

database = config.get('sqlite','database')
table    = config.get('sqlite','table')

def write_to_sqlite():

    stmt_create = """
        CREATE TABLE teste (
            id integer PRIMARY KEY,
            name text NOT NULL,
            begin_date text,
            end_date text)
        """

    # stmt_insert =""" """

    try:
        con = sqlite3.connect(database)
        cur = con.cursor()
        cur.execute(stmt_create)
        cur.commit()
    
        cur.execute()
    
        con.close()
    except Exception as e:
        log.logger.exception('Falha ao gravar no SQLite: ' + str(e))
 