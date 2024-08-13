# TechGuard Security Solutions - Ferramenta de Monitoramento de Segurança

Este projeto é uma aplicação básica em Python para monitoramento de segurança, desenvolvida para a empresa TechGuard Security Solutions.

## Estrutura do Projeto

- `app.py`: Script principal que inicia o monitoramento.
- `config/config.yaml`: Arquivo de configuração com parâmetros para o monitoramento.
- `monitor/monitor.py`: Lógica de monitoramento e envio de alertas.
- `config_loader.py`: Script para carregar a configuração YAML.
- `logs/system.log`: Arquivo de log monitorado pela aplicação.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório.
3. Edite o arquivo `config/config.yaml` com as configurações desejadas.
4. Execute o script `app.py`:
   ```bash
   python app.py
   ```

## Requisitos

- Python 3.7+
- Bibliotecas: `PyYAML`, `smtplib`
- Acesso à internet para envio de e-mails de alerta.

## Funcionamento

A aplicação monitora o arquivo de log especificado e envia um alerta por e-mail se o número de eventos suspeitos detectados atingir o limite configurado. O monitoramento é realizado a cada 60 segundos.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto é licenciado sob a MIT License.
