# Ifood Web Scrapper

Esse é um web scrapper que irá inspensionar a página de um determinado restaurante do Ifood e retornar um arquivo .csv com dados dos produtos, e suas respectivas categorias, descrições, e preços. (Ainda em desenvolvimento)

## Instalação

1. Para baixar todos os pacotes, crie um virtual environment usando este comando:

```powershell
python -m venv env_ifood
```

2. Ative o virtual enviroment 

(Linux)
```bash
source env_ifood/bin/activate
```

(Windows)
```powershell
env_name\Scripts\Activate.ps1
```

3. Use este comando para instalar todos os pacotes necessários:

```bash
pip install -r requirements.txt
```

4. Rode o código

```bash
python main.py
```