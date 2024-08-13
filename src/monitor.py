import re
import smtplib
from email.mime.text import MIMEText

def monitor_log(log_file, threshold, recipients):
    try:
        with open(log_file, 'r') as file:
            log_data = file.read()

        pattern = re.compile(r"ERRO|FALHA|INVASÃO")
        matches = pattern.findall(log_data)

        if len(matches) >= threshold:
            send_alert(recipients, len(matches))

    except FileNotFoundError:
        print(f"Arquivo de log {log_file} não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro durante o monitoramento: {e}")

def send_alert(recipients, count):
    message = MIMEText(f"Foram detectados {count} eventos suspeitos no sistema.")
    message['Subject'] = 'Alerta de Segurança'
    message['From'] = 'alerta@techguard.com'
    message['To'] = ', '.join(recipients)

    try:
        server = smtplib.SMTP('smtp.techguard.com', 587)
        server.starttls()
        server.login('alerta@techguard.com', 'senha_super_secreta')
        server.sendmail('alerta@techguard.com', recipients, message.as_string())
        server.quit()
        print("Alerta enviado com sucesso.")
    except Exception as e:
        print(f"Falha ao enviar alerta: {e}")
