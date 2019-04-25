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

def email(subj, text):

    e_user = config.get('email','user')
    e_pass = config.get('email','pass')
    e_smtp = config.get('email','smtp')
    e_dest = config.get('email','dest').split(',')
    e_logo = config.get('email','logo')

    try:
        msg = MIMEMultipart()
        msg['Subject'] = subj
        msg['From'] = e_user
        msg['To'] = ','.join(e_dest)
        
        
        with open(e_logo, 'rb') as f:
            mime = MIMEBase('image', 'png', filename='e_logo.png')
            mime.add_header('Content-Disposition', 'attachment', filename='img1.png')
            mime.add_header('X-Attachment-Id', '0')
            mime.add_header('Content-ID', '<0>')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            msg.attach(mime)

        msg.attach(MIMEText(text, 'html'))    
        server = smtplib.SMTP(e_smtp)
        server.starttls()
        server.login(e_user, e_pass)
        server.sendmail(msg['From'], e_dest, msg.as_string())
        server.quit()
        log.logger.info('Email enviado com sucesso!' )

    except Exception as e:
        log.logger.exception('Falha no envio do email: ' + str(e))
