# -*- coding: utf-8 -*-

import pandas as pd

import libs.ana_class_atest_log as log

import configparser
config = configparser.RawConfigParser(allow_no_value=True)
config.read('./conf/ana_class_atest.cfg')


def empregados_to_pandas():
    
    empregados = config.get('arquivos','tabela_empregados')
    df = pd.read_csv(empregados, sep=',', dtype=str)
    return df


def atestados_to_pandas():
    
    atestados  = config.get('arquivos','tabela_atestados')
    df = pd.read_csv(atestados, sep=',', dtype=str)
    return df


def atestados_empregados_merged():
     
    ate = atestados_to_pandas()
    emp = empregados_to_pandas()
    mer = pd.merge(ate, emp, how='left', left_on=['chapa'], right_on=['CPF'])
    return mer
