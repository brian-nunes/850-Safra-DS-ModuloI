import json
import os.path
import sys

def obter_dados():
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados: list) -> list:
    categorias = []

    for produto in dados:
        if produto["categoria"] not in categorias:
            categorias.append(produto["categoria"])

    return categorias

def listar_por_categoria(dados: list, categoria: str) -> list:
    produtos = []

    for produto in dados:
        if produto["categoria"] == categoria:
            produtos.append(produto)

    return produtos
    
def produto_mais_caro(dados: list, categoria: str) -> dict:
    produtos = listar_por_categoria(dados, categoria)
    return sorted(produtos, key = lambda x: float(x["preco"]), reverse=True)[0]


def produto_mais_barato(dados: list, categoria: str) -> dict:
    produtos = listar_por_categoria(dados, categoria)
    return sorted(produtos, key = lambda x: float(x["preco"]))[0]

def top_10_caros(dados: list) -> list:
    return sorted(dados, key = lambda x: float(x["preco"]), reverse=True)[:10]

def top_10_baratos(dados: list) -> list:
    return sorted(dados, key = lambda x: float(x["preco"]))[:10]

def print_categoria(opcao: str, categoria: str, resposta: list | dict) -> None:
    if type(resposta) == list:
        print(f"\nA lista de produtos da categoria {categoria} é:")
        for produto in resposta:
            print(f"ID: {produto['id']} | Preço: R${produto['preco']}")
    else:
        print(f"\nO produto mais {'caro' if opcao == '3' else 'barato'} da categoria {categoria} é:")
        print(f"ID: {resposta['id']} | Preço: R${resposta['preco']}")

def print_sem_categoria(opcao: str, resposta: list) -> None:
    if len(resposta) > 0 and type(resposta[0]) == dict:
        print(f"\nOs top 10 mais {'caro' if opcao == '5' else 'barato'} são:")
        for idx, produto in enumerate(resposta):
            print(f"{idx+1} | ID: {produto['id']} | Preço: R${produto['preco']} | Categoria: {produto['categoria']}")
    elif len(resposta) > 0 and type(resposta[0]) == str:
        print("\nA lista de categorias é:")
        for categoria in resposta:
            print(categoria)
    else:
        print("\nNão encontramos resposta!")

def pega_opcao() -> str:
    print("\nDigite a opção desejada: \n",
        "1. Listar categorias\n",
        "2. Listar produtos de uma categoria\n",
        "3. Produto mais caro por categoria\n",
        "4. Produto mais barato por categoria\n",
        "5. Top 10 produtos mais caros\n",
        "6. Top 10 produtos mais baratos\n",
        "0. Sair\n")
    return input()

def menu(dados):
    opcoes = {
        "1": listar_categorias,
        "2": listar_por_categoria,
        "3": produto_mais_caro,
        "4": produto_mais_barato,
        "5": top_10_caros,
        "6": top_10_baratos
    }

    opcao = pega_opcao()
    while opcao != "0":
        if opcao not in opcoes and opcao != "0":
            print("Opção inválida!")
            opcao = pega_opcao()
            continue

        if opcao in list("234"):
            categoria = input("Qual categoria deseja? ")
            resposta = opcoes[opcao](dados, categoria)
            print_categoria(opcao, categoria, resposta)
        else:
            resposta = opcoes[opcao](dados)
            print_sem_categoria(opcao, resposta)

        opcao = pega_opcao()
    else:
        print("Obrigado por usar o programa!")



# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)
