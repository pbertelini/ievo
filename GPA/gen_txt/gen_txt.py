# -*- coding: utf-8 -*-

import pandas as pd

import gen_txt_log as log

from gen_txt_sources import get_from_mssql, get_from_file
from gen_txt_util import prev_day
from gen_txt_sftp import upload

import configparser
config = configparser.RawConfigParser(allow_no_value=True)
config.read('gen_txt.cfg')

prefixo_saida  = config.get('arquivos','prefixo_saida')
extensao_saida = config.get('arquivos','extensao_saida')


def ini():
    log.logger.info("=" * 50)
    log.logger.info("     GENERATE TXT FROM SQL [IEVO] - INI")
    log.logger.info("=" * 50)


def fim():
    log.logger.info("=" * 50)
    log.logger.info("     GENERATE TXT FROM SQL [IEVO] - FIM")
    log.logger.info("=" * 50)


if __name__ == "__main__":

    ini()

    from_sql  = get_from_mssql()
    from_file = get_from_file()
    diff_file = []

    log.logger.info('Diferencas:')
    
    for sql_index, sql_row in from_sql.iterrows():        
        for file_index, file_row in from_file.iterrows():

            if ((int(sql_row['LOJA'])      == int(file_row['COD-LOJA'])) and
                (int(sql_row['PLU'])       == int(file_row['COD-PLU']))  and
                (int(sql_row['QDE_EMBAL']) != int(file_row['QTD-EMBAL']))):
                
                d = '1'                                     + ';' + \
                    str(file_row['COD-DEP'])                + ';' + \
                    str(file_row['COD-LOJA'])               + ';' + \
                    str(file_row['COD-BAND'])               + ';' + \
                    str(file_row['COD-FABRIC'])             + ';' + \
                    str(file_row['COD-PROD'])               + ';' + \
                    str(file_row['COD-PLU'])                + ';' + \
                    str(file_row['NOME-PROD'])              + ';' + \
                    str(file_row['QTD-SUGESTAO'])           + ';' + \
                    str(file_row['UNI-EMBAL'])              + ';' + \
                    str(file_row['OP'])                     + ';' + \
                    str(file_row['DATA-PED'])               + ';' + \
                    str(file_row['USU-PED'])                + ';' + \
                    str(file_row['PROG-PED'])               + ';' + \
                    str(file_row['TIP-FATUR'])              + ';' + \
                    str(int(sql_row['QDE_EMBAL'])).zfill(6) + ';' + \
                    str(file_row['ISN'])                    + ';' + \
                    '            1'
                diff_file.append(d)
                log.logger.info(d)

    log.logger.info('Verificacao concluida.')

    if len(diff_file) > 0:
        file_name = prefixo_saida + prev_day() + extensao_saida
        f_out = open(file_name, 'w')
        for line in diff_file:
            f_out.write(line + '\n')
        f_out.close()
        upload(file_name)
    else:
        log.logger.info("Arquivo vazio... Upload cancelado.")
   
    fim()
