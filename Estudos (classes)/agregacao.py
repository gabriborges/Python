class CarringoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produtos(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

class Produto:
    def __init__(self,nome,valor):
        self.nome = nome
        self.valor = valor


carrinho = CarringoDeCompras()
p1=Produto('notebook','2159.00')
carrinho.inserir_produtos(p1)

carrinho.lista_produto()