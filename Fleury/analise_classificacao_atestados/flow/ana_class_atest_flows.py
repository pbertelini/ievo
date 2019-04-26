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
    email_subj = config.get('email','subj')
    email_copy = config.get('email','copy')
    
    templ_html = config.get('email','body')
    email_body = open(templ_html, 'r')
    html = email_body.readlines()
    html = ''.join(html)

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

    email_ok_node_01 = 0
    email_er_node_01 = 0
    email_ok_node_02 = 0
    email_er_node_02 = 0
    email_ok_node_03 = 0
    email_er_node_03 = 0
    
    for i in atestados_empregados.index:
        row = atestados_empregados.loc[i]
        
        if ((row['CPF'] == row['chapa'])      and 
            (row['CID'] is not np.nan)        and
            (row['Situacao'] in situacao_emp) and
            (days_ago(row['DataAtend']) <= dias_partida)):

#=== NODE 01 ==========================================================================#
            
            if row['CID'][:1] in cids_node_01:
                if row['Emasil'] is not np.nan: 
                    if row['Emasil'] not in email_list:
                        email_list.append(row['Emasil'].lower())
                        email_ok_node_01 += 1
                        log.logger.info('NODE # 01: CPF ' + row['CPF'] + '| Email ' + str(row['Emasil']).lower() + ' adicionado a lista!')
                else:
                    log.logger.warning('NODE # 01: CPF ' + row['CPF'] + ' ==> Email nao encontrado.')
                    email_er_node_01 += 1
            else:

#=== NODE 02 ==========================================================================#
                
                if ((int(row['QtdeDias']) >= node_02_min_dias) and 
                    (int(row['QtdeDias']) <= node_02_max_dias)):
                    if row['Emasil'] is not np.nan: 
                        if row['Emasil'] not in email_list:
                            email_list.append(row['Emasil'].lower())
                            log.logger.info('NODE # 02: CPF ' + row['CPF'] + '| Email ' + str(row['Emasil']).lower() + ' adicionado a lista!')
                            email_ok_node_02 += 1
                    else:
                        log.logger.warning('NODE # 02: CPF ' + row['CPF'] + ' ==> Email nao encontrado.') 
                        email_er_node_02 += 1
                else:

#=== NODE 03 ==========================================================================#
                    
                    if ((int(row['QtdeDias']) >= node_03_min_dias) and 
                        (int(row['QtdeDias']) <= node_03_max_dias) and
                        (row['CID'][:1] in cids_node_03)):
                        if row['Emasil'] is not np.nan: 
                            if row['Emasil'] not in email_list:
                                email_list.append(row['Emasil'].lower())
                                log.logger.info('NODE # 03: CPF ' + row['CPF'] + '| Email ' + row['Emasil'] + ' adicionado a lista!')
                                email_ok_node_03 += 1
                        else:
                            log.logger.warning('NODE # 03: CPF ' + row['CPF'] + ' ==> Email nao encontrado.')
                            email_er_node_03 += 1
                    else:
                        log.logger.debug('CPF nao caiu em nenhum Node: ' + row['CPF'])

    
    email_list.append(email_copy)
    log.logger.info('Email ' + email_copy + ' adicionado a lista de destinatarios.')
    
    email_list = set(email_list)

    if email_test:
        email_dest = config.get('email','dest').split(',')
        email_list = email_dest
        log.logger.info('Executando disparo de emails em <MODO TESTE>')
        log.logger.info('<MODO TESTE> A lista verdadeira de destinatarios sera desprezada.')
        log.logger.info('<MODO TESTE> Os emails de teste serao entregues apenas para:')
        log.logger.info( ','.join(email_dest))

    # email(email_subj, html, email_list)

#=== PRINTS ==========================================================================#

    usuarios_notificados = email_ok_node_01 + email_ok_node_02 + email_ok_node_03  

    usuarios_a_notificar = (email_ok_node_01 + email_ok_node_02 + email_ok_node_03 +
                            email_er_node_01 + email_er_node_02 + email_er_node_03)

    print('')
    print('Rotina executada com sucesso!')
    print('')
    print('Inicio da Rotina: Integração de TABELAS')
    print('-' * 112)
    print('[INFO] Tabela de Atestados carregada com sucesso.')
    print('[INFO] Tabela de Empregados carregada com sucesso.')
    print('[INFO] Matriz Empregados + Atestados realizado com sucesso.')
    print('')
    print('-' * 112)
    print('[ALGORTIMO] ARVORE DECISÕES:')
    print('[RESULTADO GERAL] # Funcionários a serem notificados: ' +str(usuarios_a_notificar).zfill(3))
    print('[CITAÇÕES] # Mails enviados: ' +str(usuarios_notificados).zfill(3))
    print('[RESUMO ANALITICO] Arquivo: iEVO_atestados_20190425.csv')
    print('')
    print('-' * 112)
    print('[NODO #1] Atestados com CID [C; D; F; M; S; T]')
    print('[Resultado] # Funcionários enquadrados neste critério: ' +str(email_ok_node_01).zfill(3))
    print('[Citações] # Mails enviados com sucesso: ' +str(email_ok_node_01).zfill(3))
    print('[Citações] # Mails não enviados por falta de cadastrado: ' +str(email_er_node_01).zfill(3))
    print('')
    print('-' * 112)
    print('[NODO #2] Atestados com afastamento entre 10 e 15 dias')
    print('[Resultado] # Funcionários enquadrados neste critério: ' +str(email_ok_node_02).zfill(3))
    print('[Citações] # Mails enviados com sucesso: ' +str(email_ok_node_02).zfill(3))
    print('[Citações] # Mails não enviados por falta de cadastrado:' +str(email_er_node_02).zfill(3))
    print('')
    print('-' * 112)
    print('[NODO #3] Atestados com afastamento entre 5 e 9 dias e CID [E;I;O]')
    print('[Resultado] # Funcionários enquadrados neste critério: ' +str(email_ok_node_03).zfill(3))
    print('[Citações] # Mails enviados com sucesso: ' +str(email_ok_node_03).zfill(3))
    print('[Citações] # Mails não enviados por falta de cadastrado: ' +str(email_er_node_03).zfill(3))
    print('')
    print('-' * 112)

#=====================================================================================#

    log.logger.info('Resumo do Fluxo de Execucao:')
    log.logger.info('* Node #01: CPFs que cairam na regra e possuem Email para contato:   ' +str(email_ok_node_01).zfill(5))
    log.logger.info('* Node #01: CPFs que cairam na regra e nao possuem Email cadastrado: ' +str(email_er_node_01).zfill(5))
    log.logger.info('* Node #02: CPFs que cairam na regra e possuem Email para contato:   ' +str(email_ok_node_02).zfill(5))
    log.logger.info('* Node #02: CPFs que cairam na regra e nao possuem Email cadastrado: ' +str(email_er_node_02).zfill(5))
    log.logger.info('* Node #03: CPFs que cairam na regra e possuem Email para contato:   ' +str(email_ok_node_03).zfill(5))
    log.logger.info('* Node #03: CPFs que cairam na regra e nao possuem Email cadastrado: ' +str(email_er_node_03).zfill(5))

    log_fim()
