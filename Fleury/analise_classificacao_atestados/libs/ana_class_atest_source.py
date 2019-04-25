# -*- coding: utf-8 -*-

import sys
import pandas as pd

import libs.ana_class_atest_log as log

import configparser
config = configparser.RawConfigParser(allow_no_value=True)
config.read('./conf/ana_class_atest.cfg')


def empregados_to_pandas():
    
    try:
        empregados = config.get('arquivos','tabela_empregados')
        df = pd.read_csv(empregados, sep=',', dtype=str)
        log.logger.info('Tabela de Empregados carregada com sucesso.')
        return df
    except Exception as e:
        log.logger.exception('Falha ao Obter tabela de Empregados: ' +str(e))
        sys.exit(0)

def atestados_to_pandas():
    
    try:
        atestados  = config.get('arquivos','tabela_atestados')
        df = pd.read_csv(atestados, sep=',', dtype=str)
        log.logger.info('Tabela de Atestados carregada com sucesso.')
        return df
    except Exception as e:
        log.logger.exception('Falha ao Obter tabela de Atestados: ' +str(e))
        sys.exit(0)


def atestados_empregados_merged():
     
    try:
        ate = atestados_to_pandas()
        emp = empregados_to_pandas()
        log.logger.info('Merge de tabelas Empregados + Atestados realizado com sucesso.')
        mer = pd.merge(ate, emp, how='left', left_on=['chapa'], right_on=['CPF'])
        return mer
    except Exception as e:
        log.logger.exception('Falha ao realizar Merge das tabelas de Empregado x Atestado: ' +str(e))
        sys.exit(0)
