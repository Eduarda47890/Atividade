class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def repor(self, qtd):
        self.estoque += qtd

    def mostrar_estoque(self):
        print(f"Estoque atual do produto {self.nome}: {self.estoque} unidades")

    def comprar(self, qtd):
        if qtd <= self.estoque:
            self.estoque -= qtd
            print(f"Compra realizada: {qtd} unidades de {self.nome}")
        else:
            print(f"Erro: estoque insuficiente para comprar {qtd} unidades de {self.nome}")

