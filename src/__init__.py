# __init__.py

"""
Este módulo é responsável por inicializar o pacote de monitoramento
de segurança da TechGuard Security Solutions.
"""

from .monitor import monitor_log, send_alert

__all__ = ["monitor_log", "send_alert"]
