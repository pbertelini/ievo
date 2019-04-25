# -*- coding: utf-8 -*-

import configparser
config = configparser.RawConfigParser(allow_no_value=True)
config.read('./conf/ana_class_atest.cfg')


from datetime import datetime as dt

def today(srt=False):
    r = dt.now().date()
    if str:
        r = str(r)
    return r


def weekday(date):
    r = today.weekday()
    return r


def prev_day():
    today = dt.now().date()
    dias_para_tras = config.getint('parms_fluxo1','dias_para_tras')
    yesterday = today + td(days=-dias_para_tras)
    return str(yesterday).replace('-','')
    