import yaml

def load_config(file_path):
    try:
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError:
        print(f"Arquivo de configuração {file_path} não encontrado.")
        return {}
    except yaml.YAMLError as e:
        print(f"Erro ao carregar o arquivo YAML: {e}")
        return {}
