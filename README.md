# TechGuard Security Monitoring

## Visão Geral

Este projeto tem como objetivo monitorar logs de sistemas para detectar atividades suspeitas em tempo real e alertar a equipe de TI.

## Estrutura

- **config/**: Contém as configurações do sistema.
- **src/**: Contém o código-fonte principal.
- **tests/**: Contém os testes unitários para o código-fonte.
- **logs/**: Diretório onde os logs do monitoramento são armazenados.

## Configuração

1. Clone o repositório:

   ```bash
   git clone https://github.com/username/techguard-security-monitoring.git
   cd techguard-security-monitoring
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure o arquivo `config.yaml` com as informações necessárias para a empresa.

## Execução

Execute o script principal:

```bash
python src/monitor.py
```
