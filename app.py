import time
from src.monitor import monitor_log
from config_loader import load_config

def main():
    config = load_config("config/config.yml")
    log_file = config.get('log_file_path', 'logs/system.log')
    threshold = config.get('alert_threshold', 5)
    recipients = config.get('email_recipients', [])

    print("Monitoramento iniciado...")
    while True:
        monitor_log(log_file, threshold, recipients)
        time.sleep(60)  # Verifica a cada 60 segundos

if __name__ == "__main__":
    main()
