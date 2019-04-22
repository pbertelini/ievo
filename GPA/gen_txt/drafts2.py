# -*- coding: utf-8 -*-

from gen_txt_sources import get_from_mssql, get_from_file

a = get_from_file()

# print(a.columns)

print(a.head())