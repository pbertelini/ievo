# -*- coding: utf-8 -*-

from ana_class_atest_source import empregados_to_pandas, atestados_to_pandas

emp = empregados_to_pandas()
ate = atestados_to_pandas()

print()
print('empregados:')
print()
print(emp.columns)
print()
print('atestados:')
print()
print(ate.columns)

