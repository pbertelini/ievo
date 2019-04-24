# -*- coding: utf-8 -*-

import ana_class_atest_log as log

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import configparser
config = configparser.RawConfigParser(allow_no_value=True)
config.read('../conf/ana_class_atest.cfg')

def email(subj, text):

    e_user = config.get('email','user')
    e_pass = config.get('email','pass')
    e_smtp = config.get('email','smtp')
    e_dest = config.get('email','dest').split(',')

    try:
        msg = MIMEMultipart()
        msg['Subject'] = subj
        msg['From'] = e_user
        msg['To'] = ','.join(e_dest)
        msg.attach(MIMEText(text))
        server = smtplib.SMTP(e_smtp)
        server.starttls()
        server.login(e_user, e_pass)
        server.sendmail(msg['From'], e_dest, msg.as_string())
        server.quit()
        log.logger.info('Email enviado com sucesso!' )

    except Exception as e:
        log.logger.exception('Falha no envio do email: ' + str(e))
