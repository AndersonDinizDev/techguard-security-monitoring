import yaml
import logging.config
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from alert import send_alert

logging.config.fileConfig('config/logging.conf')
logger = logging.getLogger(__name__)

with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

class LogMonitorHandler(FileSystemEventHandler):
    def __init__(self, alert_threshold):
        self.suspect_count = 0
        self.alert_threshold = alert_threshold

    def on_modified(self, event):
        with open(config['log_file_path'], 'r') as file:
            lines = file.readlines()
            last_line = lines[-1]
            if "SUSPICIOUS" in last_line:
                self.suspect_count += 1
                logger.warning(f"Atividade suspeita detectada: {last_line.strip()}")
                if self.suspect_count >= self.alert_threshold:
                    send_alert(self.suspect_count)
                    self.suspect_count = 0

if __name__ == "__main__":
    event_handler = LogMonitorHandler(alert_threshold=config['alert_threshold'])
    observer = Observer()
    observer.schedule(event_handler, path=config['log_file_path'], recursive=False)
    observer.start()
    logger.info("Monitoramento de logs iniciado.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
