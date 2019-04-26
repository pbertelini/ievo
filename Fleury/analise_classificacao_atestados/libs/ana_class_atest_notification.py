# -*- coding: utf-8 -*-

from libs import ana_class_atest_log as log

import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

import configparser
config = configparser.RawConfigParser(allow_no_value=True)
config.read('./conf/ana_class_atest.cfg')

def email(subj, text, dest):

    try:
        e_from = config.get('email','from')
        e_user = config.get('email','user')
        e_pass = config.get('email','pass')
        e_smtp = config.get('email','smtp')
        
        cabecalho = config.get('email','cabecalho')
        rodape    = config.get('email','rodape')
        
        msg = MIMEMultipart()
        msg['Subject'] = subj
        msg['From'] = e_from
        msg['To'] = e_user

        with open(cabecalho, 'rb') as f:
            mime = MIMEBase('image', 'png', filename='cabecalho.png')
            mime.add_header('Content-Disposition', 'attachment', filename=cabecalho)
            mime.add_header('X-Attachment-Id', '1')
            mime.add_header('Content-ID', '<1>')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            msg.attach(mime)

        with open(rodape, 'rb') as f:
            mime = MIMEBase('image', 'png', filename='rodape.png')
            mime.add_header('Content-Disposition', 'attachment', filename=rodape)
            mime.add_header('X-Attachment-Id', '0')
            mime.add_header('Content-ID', '<0>')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            msg.attach(mime)
        
        msg.attach(MIMEText(text, 'html'))    
        server = smtplib.SMTP(e_smtp)
        server.starttls()
        server.login(e_user, e_pass)
        server.sendmail(msg['From'], [] + dest, msg.as_string())
        server.quit()
        log.logger.info('Email(s) enviado(s) com sucesso!' )

    except Exception as e:
        log.logger.exception('Falha no envio do(s) email(s): ' + str(e))
