# -*- coding: utf-8 -*-

import sys
import pymssql
import pandas as pd

import gen_txt_log as log

from gen_txt_util import prev_day, unzip
from gen_txt_sftp import download

import configparser
config = configparser.RawConfigParser(allow_no_value=True)
config.read('gen_txt.cfg')

def get_from_mssql():

    try:
    
        log.logger.info('Obtendo dados do MSSQL...')
    
        hostname = config.get('mssql','hostname')
        username = config.get('mssql','username')
        password = config.get('mssql','password')
        database = config.get('mssql','database')
    
        conn = pymssql.connect(hostname, username, password, database)
        stmt = ("""
            select 
                loja as LOJA, 
                cod_plu as PLU , 
                cast( ROUND(qtd_plts / plts_cx,0 ) as int ) as QDE_EMBAL 
            from 
                ievo_gpa_prod.dbo.Tabela_Relacionada_Depois 
            where 
                cast( ROUND(qtd_plts / plts_cx,0 ) as int ) > 0
        """)
            
        df = pd.read_sql(stmt,conn)
        return df
    
    except Exception as e:
        log.logger.exception('Falha ao obter dados do MSSQL: ' + str(e))
        sys.exit(0)

def get_from_file():
    
    try:
        
        log.logger.info('Obtendo dados do arquivo de Entrada...')
        
        prefixo_entrada  = config.get('arquivos','prefixo_entrada')
        extensao_entrada = config.get('arquivos','extensao_entrada')
        file_name = prefixo_entrada + prev_day() + extensao_entrada
        
        download(file_name)
        unzip(file_name)
        
        txt_file = file_name.replace('.gz','')
        content  = []
        txt = open(txt_file, 'r')
        content =  txt.readlines()
        content.pop(0)
        content.pop(0)
        content.pop(-1)
        txt.close()

        txt_out = open(txt_file, 'w')
        for line in content:
            txt_out.write(line[2:136] + '\n')
        txt_out.close()
    
        df = pd.read_csv(txt_file, header=None, sep=';', names=[
            'COD-DEP','COD-LOJA','COD-BAND','COD-FABRIC','COD-PROD','COD-PLU',
            'NOME-PROD','QTD-SUGESTAO','UNI-EMBAL','OP','DATA-PED','USU-PED',
            'PROG-PED','TIP-FATUR','QTD-EMBAL','ISN'])

        dfs = df.groupby(['COD-LOJA', 'COD-PLU'], as_index=False)[['QTD-EMBAL']].sum()      
        dfs.to_csv('teste_com_sumarizacao.csv')
        
        return dfs

    except Exception as e:
        log.logger.exception('Falha ao obter dados do arquivo de Entrada: ' + str(e))
        sys.exit(0)
