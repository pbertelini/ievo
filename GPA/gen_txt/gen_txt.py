# -*- coding: utf-8 -*-

import pandas as pd

from gen_txt_sources import get_from_mssql, get_from_file
from gen_txt_util import prev_day
from gen_txt_sftp import upload

import configparser
config = configparser.RawConfigParser(allow_no_value=True)
config.read('gen_txt.cfg')

prefixo_saida  = config.get('arquivos','prefixo_saida')
extensao_saida = config.get('arquivos','extensao_saida')


if __name__ == "__main__":

    from_sql  = get_from_mssql()
    from_file = get_from_file()
    
    print(from_sql.dtypes)
    print('')
    print(from_file.dtypes)
    
    # comparar datasets
    
    # for line in range(len(from_file)):
    #     print(from_sql[line])
    
    # file_name = prefixo_saida + prev_day() + extensao_saida
    # upload(file_name)
