# -*- coding: utf-8 -*-

import sys
import gzip
import shutil

import gen_txt_log as log

from datetime import datetime as dt
from datetime import timedelta as td


def prev_day():

    try:
        today = dt.now().date()
        yesterday = today + td(days=-2)
        return str(yesterday).replace('-','')
    except Exception as e:
        log.logger.exception('Falha ao obter dia anterior: ' + str(e))
        sys.exit(0)

def unzip(file_path):

    try:    
        with gzip.open(file_path, 'rb') as f_in:
            with open(file_path.replace('.gz',''), 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        log.logger.info('Arquivo descompactado: ' + str(file_path))
    except Exception as e:
        log.logger.exception('Falha ao descompactar arquivo: ' + str(e))
        sys.exit(0)

