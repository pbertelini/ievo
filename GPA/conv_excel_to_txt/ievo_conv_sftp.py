# -*- coding: utf-8 -*-

import paramiko

import ievo_conv_log as log

import configparser
config = configparser.RawConfigParser(allow_no_value=True)
config.read('ievo_conv.cfg')   

sftp_host  = config.get('sftp','sftp_host')
sftp_user  = config.get('sftp','sftp_user')
public_key = config.get('sftp','public_key')
remote_dir = config.get('sftp','remote_dir')

def upload(local_file):
    
    log.logger.info('Iniciando transferencia sFTP...')
    log.logger.info('Arquivo Local: ' + local_file)
    log.logger.info('Arquivo Remoto: ' + remote_dir + local_file)
    
    upload_ok = False
    
    try:
    
        ssh_client=paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        ssh_client.connect(
            hostname=sftp_host,
            username=sftp_user,
            key_filename=public_key)
        
        ftp_client=ssh_client.open_sftp()
        ftp_client.put(local_file, remote_dir + local_file)
        ftp_client.close()
        log.logger.info('Upload realizado com sucesso!')
        upload_ok = True

    except Exception as e:
        log.logger.exception('Falha ao conectar no Servidor sFTP: ' + str(e))
        
    return upload_ok
