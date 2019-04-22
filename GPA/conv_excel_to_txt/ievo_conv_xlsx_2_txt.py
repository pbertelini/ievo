# -*- coding: utf-8 -*-

import sys
import pandas as pd
import ievo_conv_log as log

from ievo_conv_layout import layouts_fixos
from ievo_conv_sftp import upload

def inicio():
    log.logger.info("=" * 50)
    log.logger.info("     CONVERSOR DE XLS PARA TXT [IEVO] - INICIO")
    log.logger.info("=" * 50)


def fim():
    log.logger.info("=" * 50)
    log.logger.info("     CONVERSOR DE XLS PARA TXT [IEVO] - FIM")
    log.logger.info("=" * 50)
    sys.exit(0)
  

def fmt_coluna(col, i):

    tipo, tam = layouts_fixos[layout][i].split('.')
  
    if tipo == "A":
        c = col.str.ljust(int(tam))
        
    if tipo == "N":
        c = col.str.zfill(int(tam))

    if tipo == "F":
        c = " " * int(tam)

    return c

if __name__ == "__main__":

    inicio()

    if len(sys.argv) != 3:
        log.logger.info("Parametros invalidos!")
        log.logger.info("Parametro 01 ==> Planilha Excel.")
        log.logger.info("Parametro 02 ==> Layout Desejado.")
        log.logger.info("Saindo...")
        fim()

    if not "XLS" in sys.argv[1].upper()[-4:]:
        log.logger.info("Parametro 01 invalido ==> Informar uma planilha Excel.")
        log.logger.info("Saindo...")
        fim()
        

    if sys.argv[2].upper() not in layouts_fixos:
        log.logger.info("Parametro 02 invalido ==> Layout nao Cadastrado.")
        log.logger.info("Layout(s) Valido(s):")
        for l in layouts_fixos:
            log.logger.info(l)
        log.logger.info("Saindo...")
        fim()
    
    log.logger.info("Parametros de entrada OK!")
    
    xls_name = str(sys.argv[1])
    log.logger.info("Planilha: " + xls_name)
    
    txt_name = xls_name.replace('.xlsx','.txt')
    
    layout = str(sys.argv[2]).upper()
    log.logger.info("Layout: " + layout)
    
    try:   
        df = pd.read_excel(xls_name, header=None, dtype=str)
        log.logger.info("Excel carregado com Sucesso.")
    except Exception as e:
        log.logger.exception("Falha ao carregar o Excel:" + str(e))
        fim()
    
    for i in range(len(df.columns)):
        df[i] = fmt_coluna(df[i], i)
        
    try:
        df.to_csv(txt_name, sep=';', header=None, index=None)
        log.logger.info("Arquivo Texto: " + txt_name)
    except Exception as e:
        log.logger.exception("Falha ao criar arquivo de Texto:" + str(e))
        fim()
    
    upload(txt_name)
    
    fim()
