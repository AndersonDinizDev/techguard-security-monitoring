import time
from monitor.monitor import monitor_log
from config_loader import load_config

def main():
    config = load_config("config/config.yaml")
    log_file = config['log_file_path']
    threshold = config['alert_threshold']
    recipients = config['email_recipients']

    print("Monitoramento iniciado...")
    while True:
        monitor_log(log_file, threshold, recipients)
        time.sleep(60)  # Verifica a cada 60 segundos

if __name__ == "__main__":
    main()
