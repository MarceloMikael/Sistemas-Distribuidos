import requests

base_url = 'http://localhost:8080/rural'

imovel = {
    "id": "202",
    "endereco": "Br-222, 999",
    "preco": 450000,
    "proprietario": {
        "nome": "Lucas Ferreira",
        "cpf": "11122233344"
    }
}

comprador = {
    "nome": "Fernanda Souza",
    "cpf": "99988877766"
}

try:
    requests.post(f"{base_url}/imoveis", json=imovel)
    print("Imóvel cadastrado\n")

    disp = requests.get(f"{base_url}/imoveis")
    print("Disponíveis:\n", disp.json())

    requests.post(f"{base_url}/imoveis/{imovel['id']}/vender", json=comprador)
    print("\nImóvel vendido\n")

    vendas = requests.get(f"{base_url}/vendas")
    print("Vendas:\n", vendas.json())

except Exception as e:
    print("Erro:\n", e)
