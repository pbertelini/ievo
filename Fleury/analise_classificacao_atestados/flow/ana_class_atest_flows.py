# -*- coding: utf-8 -*-

import numpy as np
import configparser
config = configparser.RawConfigParser(allow_no_value=True)
config.read('./conf/ana_class_atest.cfg')


def fluxo1():

    from libs.ana_class_atest_source import atestados_empregados_merged
    from libs.ana_class_atest_util import log_ini, log_fim, days_ago
    from libs.ana_class_atest_notification import email

    from libs import ana_class_atest_log as log
    
    log_ini()
    
    email_test = config.getboolean('email','test')
    email_dest = config.get('email','dest').split(',')
    
    template_html = config.get('email','body')
    
    situacao_emp = config.get('parms_fluxo1','situacao_emp').split(',')
    cids_node_01 = config.get('parms_fluxo1','cids_node_01').split(',')
    cids_node_03 = config.get('parms_fluxo1','cids_node_03').split(',')
    dias_partida = config.getint('parms_fluxo1','dias_partida')
    
    node_02_min_dias = config.getint('parms_fluxo1','node_02_min_dias')
    node_02_max_dias = config.getint('parms_fluxo1','node_02_max_dias')
    node_03_min_dias = config.getint('parms_fluxo1','node_03_min_dias')
    node_03_max_dias = config.getint('parms_fluxo1','node_03_max_dias')
    
    email_list = []

    atestados_empregados = atestados_empregados_merged()
    for i in atestados_empregados.index:
        row = atestados_empregados.loc[i]
        
        if ((row['CPF'] == row['chapa'])      and 
            (row['CID'] is not np.nan)        and
            (row['Situacao'] in situacao_emp) and
            (days_ago(row['DataAtend']) <= dias_partida)):

#=== NODE 01 ==========================================================================#
            
            if row['CID'][:1] in cids_node_01:
                if row['Emasil'] is not np.nan and row['Emasil'] not in email_list:
                    email_list.append(row['Emasil'].lower())
            else:
            
#=== NODE 02 ==========================================================================#
                
                if ((int(row['QtdeDias']) >= node_02_min_dias) and 
                    (int(row['QtdeDias']) <= node_02_max_dias)):
                    if row['Emasil'] is not np.nan and row['Emasil'] not in email_list:
                        email_list.append(row['Emasil'].lower())    
                else:
                    
#=== NODE 03 ==========================================================================#
                    
                    if ((int(row['QtdeDias']) >= node_03_min_dias) and 
                        (int(row['QtdeDias']) <= node_03_max_dias) and
                        (row['CID'][:1] in cids_node_03)):
                        if row['Emasil'] is not np.nan and row['Emasil'] not in email_list:
                            email_list.append(row['Emasil'].lower())  
                    else:
                        pass # email com resumo p monit

    email_list = set(email_list)
    
    email_body = open(template_html, 'r')
    html = email_body.readlines()
    html = ''.join(html)
    
    if email_test:
        email_list = email_dest
    
    email('oi como q ta', html)
    
    print(len(email_list))
    print(email_list)

    log_fim()
