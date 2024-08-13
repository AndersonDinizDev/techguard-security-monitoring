import smtplib
from email.mime.text import MIMEText
import yaml
import logging

logger = logging.getLogger(__name__)

with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

def send_alert(suspect_count):
    message = f"{suspect_count} atividades suspeitas foram detectadas no sistema."
    msg = MIMEText(message)
    msg['Subject'] = 'Alerta de Segurança'
    msg['From'] = 'noreply@techguard.com'
    msg['To'] = ', '.join(config['email_recipients'])

    try:
        with smtplib.SMTP('localhost') as server:
            server.sendmail(msg['From'], config['email_recipients'], msg.as_string())
        logger.info(f"Alerta enviado para: {config['email_recipients']}")
    except Exception as e:
        logger.error(f"Erro ao enviar alerta: {e}")
