# -*- coding: utf-8 -*-

import gzip
import shutil

from datetime import datetime as dt
from datetime import timedelta as td


def prev_day():

    today = dt.now().date()
    yesterday = today + td(days=-1)
    return str(yesterday).replace('-','')


def unzip(file_path):
    
    with gzip.open(file_path, 'rb') as f_in:
        with open(file_path.replace('.gz',''), 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
