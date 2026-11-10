#Mensagem de boas vindas
print("=== BEM VINDO AO SACOLÃO DA GENERATION")

# Carregadar dados
produtos = ["Banana","Melancia","Jambolão"]
precos = [5,19,29.99]

#Etapa 3 estrutura condicionada
#Etapa 3.1 - Mostrar os produtos
for i in produtos:
    print(i)

#for de duas listas

for i,j in zip(produtos,precos):
    print(f"o produto {i} custa R${j:.2F}")

resposta = input("Deseja cadastrar novo produto?")

# Inserir novo produto
if resposta.lower() == "sim":
    novo_produto = input("Informe o nome do produto")
    novo_preco = float(input("Informe o valor"))
    print("Produto cadastro com sucesso")

#Sempre queremos colocar um novo valor na lista devemos usar o método de anexo.
#lista.anexo(novo_valor)

produtos.append(novo_produto)
precos.append(novo_preco)
for i,j in zip(produtos,precos):
    print(f"o produto {i} custa R${j:.2f}")