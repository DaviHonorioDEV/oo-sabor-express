from modelos.cardapio.item_cardapio import ItemCardapio

class sobremesa(ItemCardapio):
    def __init__(self, nome, preco, descricao, tipo, tamanho):
        super().__init__(nome, preco)
        self.descricao = descricao
        self.tipo = tipo
        self.tamanho = tamanho

    def __str__(self):
        return f'{self.nome}'

    def aplicar_desconto(self):
            """Aplica um desconto de 10% no preço da sobremesa."""
            self._preco -= (self._preco * 0.15)