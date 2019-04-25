# -*- coding: utf-8 -*-

import libs.ana_class_atest_log as log
from datetime import datetime as dt
from datetime import timedelta as td

import configparser
config = configparser.RawConfigParser(allow_no_value=True)
config.read('./conf/ana_class_atest.cfg')


def now(string=False):
    
    r = dt.now()
    if string:
        r = str(r)
    return r


def today(string=False):
    
    r = dt.now().date()
    if string:
        r = str(r)
    return r


def day_of_the_week(date=dt.now(), string=False):
    
    r = date.weekday()
    if string:
        dias_semana = {
        0 :'Segunda-feira',
        1 :'Terça-feira',
        2 :'Quarta-feira',
        3 :'Quinta-feira',
        4 :'Sexta-feira',
        5 :'Sábado',
        6 :'Domingo'}
        r = dias_semana[r]
    return r


def days_ago(data_str):
    # 2018-07-27 00:00:00
    d = dt.strptime(data_str, "%Y-%m-%d %H:%M:%S")
    h = now()
    r = (h - d).days
    return r

def log_ini():
    
    log.logger.info("=" * 65)
    log.logger.info("ANALISE E CLASSIFICACAO DE ATESTADOS <FLEURY Powered by iEVO> INI")
    log.logger.info("=" * 65) 
    

def log_fim():
    
    log.logger.info("=" * 65)
    log.logger.info("ANALISE E CLASSIFICACAO DE ATESTADOS <FLEURY Powered by iEVO> FIM")
    log.logger.info("=" * 65) 
    