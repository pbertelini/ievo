# -*- coding: utf-8 -*-

import pandas as pd

import ana_class_atest_log as log

import configparser
config = configparser.RawConfigParser(allow_no_value=True)
config.read('../conf/ana_class_atest.cfg')


def empregados_to_pandas():
    empregados = config.get('arquivos','tabela_empregados')
    df = pd.read_csv(empregados, sep=',')
    return df


def atestados_to_pandas():
    atestados  = config.get('arquivos','tabela_atestados')
    df = pd.read_csv(atestados, sep=',')
    return df
